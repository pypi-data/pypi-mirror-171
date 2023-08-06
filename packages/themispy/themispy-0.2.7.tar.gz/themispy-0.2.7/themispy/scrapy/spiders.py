from multiprocessing import Process, Queue

from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


def run_spider(spider: Spider, pipeline: str = None,
               settings: dict = None, override: bool = False) -> None:
    """
    Process for running spiders.
    
    Attributes:
        spider (scrapy.Spider): Spider class used for crawling.
        pipeline (str): Must be either 'blob' or 'download'.
        settings (dict): Scrapy Settings object.
        override (str): If set to 'True', the settings passed will
    override all previous settings.
    
    """
    if pipeline is not None and pipeline != 'blob' and pipeline !='download' and pipeline != 'append':
        raise Exception("Pipeline must be either 'blob', 'append' or 'download'.")
    
    # Configure Scrapy Project Settings
    scrapy_settings = get_project_settings()
    
    DEFAULT_SETTINGS = {
        'Accept-Language': 'pt-BR',
        'FILES_STORE': 'Khipo-Themis_Project',
        'FILES_EXPIRES': 0,
        'DOWNLOAD_TIMEOUT': 300
    }
    
    scrapy_settings.update(DEFAULT_SETTINGS)
    
    if pipeline == 'blob':
        scrapy_settings.update({
            'ITEM_PIPELINES': {f'themispy.scrapy.pipelines.AzureBlobUploadPipeline': 1}
        })
    elif pipeline == 'append':
        scrapy_settings.update({
            'ITEM_PIPELINES': {f'themispy.scrapy.pipelines.AzureAppendBlobUploadPipeline': 1}
        })
    elif pipeline == 'download':
        scrapy_settings.update({
            'ITEM_PIPELINES': {f'themispy.scrapy.pipelines.AzureFileDownloaderPipeline': 1}
        })
    
    if settings is not None:
        if override:
            scrapy_settings = get_project_settings()
        
        scrapy_settings.update(settings)
        
    print(f"[SCRAPY SETTINGS]\n{scrapy_settings.copy_to_dict()}")
    
    
    def multiprocess(queue: Queue) -> None:
        """Setup incoming spider running call for multiprocessing."""
        try:
            configure_logging(settings=scrapy_settings)
            runner = CrawlerRunner(settings=scrapy_settings)
            deferred = runner.crawl(spider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            queue.put(None)
        except Exception as e:
            queue.put(e)

    queue_ = Queue()
    process = Process(target=multiprocess, args=(queue_,))
    process.start()
    result = queue_.get()
    process.join()

    if result is not None:
        raise result
