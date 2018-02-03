from icrawler.builtin import GoogleImageCrawler
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--keyword", type=str, help="search keyword")
	parser.add_argument("--dir", type=str, help="dir")
	args = parser.parse_args()

	if args.keyword:
		keyword = args.keyword
	if args.dir:
		dir_ = args.dir

	google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
	                                    storage={'root_dir': dir_ })
	google_crawler.crawl(keyword=keyword, max_num=1000,
	                     date_min=None, date_max=None,
	                     min_size=(300,300), max_size=None)
