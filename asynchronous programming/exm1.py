import asyncio
import time

def test():
    print("Test start")
    time.sleep(10)
    print("Test ended")

def main():
    print("Start of main corouting")
    test()
    print("After test")


main()