import os

from webster.conf import settings
from webster.net.request import Request


class Downloader:
    
    """
    A class that represents Downloader module 
    used to download webpages and saving 
    webpages in html format.
    
    Attributes
    ----------
    Request : object
        Webster.net.Request object.
    
    Methods
    -------
    download
        Downloads Webster.net.Request content and saves the content as html file.  
    """
    
    def __init__(self, request: Request) -> None:
        """
        Parameters
        ----------
        Request : object
            Webster.net.Request object of the URL to download.   
        """

        self.filename = None
        self.filepath = None
        
        if not isinstance(request, Request):
            raise TypeError(
                "Expected response type of Request, instead got: "
                , type(request))
        else: 
            self.request = request
              
    def get_request(self):
        return self.request
    
    def get_filename(self):
        return self.filename
    
    def get_filepath(self):
        return self.filepath
    
    def __str__(self):
        return self.filename
          
    __repr__= __str__
       
    def download(self) -> None:
        """
        Download page content as html and store it inside the
        download folder. 
    
        Returns
        -------
        file
            Webster.net.Request contents saved in html format.
    
        """
        self.filename = self.request.url.split(
                "//")[1].replace(
                "/", "") + ".html"   
        self.filepath = settings.PATH.join(
                settings.DL_DIR, self.filename)
            
        try:
            os.makedirs(settings.DL_DIR)
        except FileExistsError:
            pass #Folder already exists not a big deal

        #Try to save the file in DL_DIR folder
        try:       
            if not settings.PATH.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    file.write(self.request.url+"\n\n")
                    file.write("File downloaded: ")
                    file.write(settings.TIME_NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                    file.write(self.request.text())

            #If the file already exists, raise error
            else: raise FileExistsError
        except FileExistsError:
            print("File exists already...")                         #SWITCH TO LOGGING
        