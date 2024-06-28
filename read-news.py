import os 
import re

def read_news(news_file):
    with open(news_file, 'r') as file:
        