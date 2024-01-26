from summarizer import Summarizer
from functools import lru_cache

#pre-loading of model to reduce the time of execution
model = Summarizer()

# Caching the results of the function to reduce the time of execution
@lru_cache(maxsize=None)
def summarize_text_with_bert(text):
    summary = model(text)
    return summary


# Example usage
# original_text = """
# Wuhan is a city in central China about the size of London, and it is here that director Weijun Chen has conducted an experiment in democracy. A grade 3 class at Evergreen Primary School has their first encounter with democracy by holding an election to select a Class Monitor. Eight-year-olds compete against each other for the coveted position, abetted and egged on by teachers and doting parents. Elections in China take place only within the Communist Party, but recently millions of Chinese voted in their version of Pop Idol. The purpose of Weijun Chen’s experiment is to determine how, if democracy came to China, it would be received. Is democracy a universal value that fits human nature? Do elections inevitably lead to manipulation? Please Vote for Me is a portrait of a society and a town through a school, its children and its families
# """

# summary = summarize_text_with_bert(original_text)

# print("Original Text:")
# print(original_text)
# print("\nSummary:")
# print(summary)
