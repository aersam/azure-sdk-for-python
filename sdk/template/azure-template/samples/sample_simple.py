"""
See https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/sample_guide.md
"""

from azure.template import template_main

def simple_sample():
    print("Running simple sample")
    template_main()
    print("Completed running simple sample")


if __name__ == "__main__":
    simple_sample()
