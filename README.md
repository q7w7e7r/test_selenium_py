Selenium Test project for http://selenium1py.pythonanywhere.com/

$ git clone https://github.com/q7w7e7r/test_selenium_py.git

---------- folder name MUST BE 'test_selenium_py' ----------

Review command example:

$ pytest -v --tb=line --language=en -m need_review

Execute command examples for Chrome browser (by default):

$ pytest -v -s --tb=line --language=en test_product_page.py

$ pytest -v -s --tb=line --language=en test_main_page.py

$ pytest -v --tb=line

Execute command examples for Firefox browser:
There are bugs in FireFox, and work is underway to fix them.
$ pytest -v -s --tb=line --browser_name=firefox --language=en test_product_page.py

$ pytest -v -s --tb=line --browser_name=firefox --language=en test_main_page.py

