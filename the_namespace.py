def test_function() :
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
test_function()
#inner_function() если вызвать вне функции test_function, то будет выдовать ошибку.