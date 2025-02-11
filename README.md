# What does it do?
Program1 adds extra functionality to the best_class() function without changing any code inside of the function. 

## What is the Code
Here is the code for the Program1:

<code> 
    def my_decorator(func):
        def wrapper():
            print("I love Animals!")
            func()
            print("And I also love golf.")
        return wrapper

        @my_decorator
            def best_class():
            print("I love Software Engineering!")

        best_class() 
</code>

### Image

![Here is an image of a dog!](https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fbreedingbusiness.com%2Fwp-content%2Fuploads%2F2021%2F07%2Fcutest-small-white-dog-breeds.jpg&sp=1739248672T34c83ad7a5be93ec17d1bf9ffdbe68a4f0c1f1f277e0a1f7af0e14b5dfaadc6b)
