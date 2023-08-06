import time
import uuid
import queue

from concurrent.futures import ThreadPoolExecutor

from typing import Optional

from webster import robotstxt
from webster.utils import validators
from webster.utils import url_tools
from webster.net.request import Request
from webster.core.parser import Parser
from webster.conf import settings


class Crawler:
    
    """
    A class that represents crawler object used to crawl websites.
    
    Attributes
    ----------
    start_urls : list
        Define starting URLs as a list. First URL in list is then defined
        as the starting point and the rest are stored in Queue.
        URLs must be in correct form: ex. https://example.com/ or https://www.example.com/
       
    allowed_urls : (Optional) list, default = None
        Define allowed URLs to visit.  
         
    mode : (Optional) str, default = auto
        Not Implemented
        
    Methods
    -------
    crawl
        Starts crawler with given starting points.
    
    """
    
    def __init__(self, 
                start_urls: list,
                allowed_urls: Optional[list] = None,
                mode: Optional[list] = None,
        ) -> None:
        
        self._ID = uuid.uuid1()
        
        
        if mode is not None:
            if validators.ModeValidator(mode):
                self.mode = mode
        else: self.mode = "auto"           
        
        if validators.URLValidator(start_urls):
            self.start_urls = start_urls
        else: self.start_urls = None
        
        if allowed_urls in [None, [""], [], [" "]]:
            self.allowed_urls = None
        elif validators.URLValidator(allowed_urls):
            self.allowed_urls = allowed_urls
        
        self.crawling = False
        
        self.queue = queue.Queue()
        
        self.responses = {}
        self.robots_allowed = {}
        self.robots_excluded = {}
    
    def _request(self, url: str) -> Request:
        """
        Helper function for making get requests.
        
        Checks if request is already made to this URL.
        """
        
        if url not in self.responses or url not in self.robots_excluded:
            #BEFORE WE MAKE THE REQUEST TO THE SERVER!!!!
            base_url = url_tools.base_url(url)
            rp = None
            
            allowed = any(base_url
                        in url_tools.base_url(s) 
                        for s 
                        in self.allowed_urls)
            
            if not allowed:
                return None
            
            if base_url not in self.robots_allowed:
                try:
                    rp = robotstxt.RobotParser(base_url + "robots.txt")
                    #Store the RobotParser object to the hashmap for later use cases.
                    self.robots_allowed[base_url] = rp
                    print(f"{self} Robots.txt found {base_url}")           #SWITCH TO LOGGING
                except ValueError:
                    print(f"{self} Robots.txt not found {base_url}")       #SWITCH TO LOGGING
                except Exception as e:
                    print(f"{self} Unexpected exception occured {base_url}:, {e}")       #SWITCH TO LOGGING
            
            if not rp or rp.allowed(url):
                delay = 0
                if settings.OBEY_ROBOTSTXT:
                    if rp is not None and rp.delay():
                        delay = rp.delay()
                
                #Send the request to the server and sleep for the time of delay parameter.
                try:
                    request = Request(url)
                    self.responses[request.url] = request
                except (ValueError, TypeError) as e:
                    print(f"{self} Error requesting {base_url}:, {e}")       #SWITCH TO LOGGING
                    return None
                
                if request.url is None:
                    return None
                
                print(f"{self} Requesting {request}")                   #SWITCH TO LOGGING
                time.sleep(delay)
                
                return request
                
            else:
                #Request did not respect the robots.txt so we skip that
                #and store the excluded url for later use.
                self.robots_excluded[base_url] = 1
                print(f"{self} Robots.txt not allowing {base_url}")       #SWITCH TO LOGGING
    
    def _start_requests(self, urls: list) -> None:
        """
        Start requesting from the given URLs.
        Send Requests to ThreadPool and execute them using threading.
        
        Put Webster.net.Request objects to queue.
        """
        
        if settings.OBEY_ROBOTSTXT:
            for url in urls:
                if url not in self.responses:
                    response = self._request(url)
                    if response is not None:
                        self.queue.put(response)
                    elif self.queue.qsize() == 0:
                        self.crawling = False

        else:
            #Create thread pool executor. Worker count matches our count of awaiting urls.
            with ThreadPoolExecutor(len(urls)) as executor:
                #Add requests to ThreadPool    
                request_futures = executor.map(lambda url : self._request(url), urls)
                #Add Crawler.Requests to queue
                _ = executor.map(self.queue.put, request_futures)
    
    def _crawl(self, rqs: Request) -> None:
        """
        Helper function for crawling.
        
        Parse request for new URLs or anchors.
        Start requesting new URLs.
        """
    
        print(f"{self} Parsing {rqs}")                                      #SWITCH TO LOGGING
        
        try:
            #Parse response anchors with Parser module.
            response_anchors = Parser(rqs).parse_anchors()
            #Store new URLs to this list later on.
            found_urls = []
            
            #If new anchors were found, add them to the list
            if response_anchors:
                for resp in response_anchors:
                    if resp not in self.responses:
                        found_urls.append(resp)
            
            if found_urls: 
                self._start_requests(found_urls)

                
        
        #Skip invalid requests where Request.body is None
        #and thus cannot be parsed.      
        except TypeError:
            print(f"{self} Skipping {rqs}")                                 #SWITCH TO LOGGING
            
    def crawl(self) -> None:
        """
        Start Webster.Crawler process from the starting urls given as
        class attributes. 
        
        If settings.OBEY_ROBOTSTXT is True Crawler will obey websites robots.txt 
        rules. User can disobey these rules by changing this settings value to False.
        Crawler will continue crawling found urls until there is not any to be found.
    
        Returns
        -------
        dict
            Dictionary of crawled websites as Webster.net.Request objects.
        """
        
        if self.crawling:
            raise RuntimeError("Already crawling!")
        self.crawling = True
        
        if self.start_urls is None:
            return None
        
        #Get requests to queue
        self._start_requests(self.start_urls)

             
        while self.crawling:
            print("Queue size:", self.queue.qsize())        #SWITCH TO LOGGING? NECESSARY????
            next_request = self.queue.get()
            
            #Check for bogus requests
            if next_request is not None:
                self._crawl(next_request)
            
            if self.queue.empty():
                self.crawling = False
            
        return self.responses
                              
    def __str__(self):
        return f"Crawler: " + str(self._ID)
        
if __name__ == "__main__":

    #anchors = list(xs.values())[0][1]

    
    url = "https://webscraper.io/test-sites"
    ws = Crawler([url], allowed_urls=["https://webscraper.io/"])                        
    xs = ws.crawl()
    print(xs)