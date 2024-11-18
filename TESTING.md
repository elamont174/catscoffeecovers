
# TESTING

## Validators
### HTML
### CSS
### Python
- [PEP8](https://pep8ci.herokuapp.com/) was used to test python files.
- All returned clear.
- ![book_reviews models.py](/images/book_reviews%20models.py.png)
- ![book_reviews serializers.py](/images/book_reviews%20serializers.py.png)
- ![book_reviews urls.py](/images/book_reviews%20urls.py.png)
- ![book_reviews views.py](/images/book_reviews%20views.py.png)
- ![catscoffeecovers permissions.py](/images/catscoffeecovers%20permissions.py.png)
- ![catscoffeecovers serializers.py](/images/catscoffeecovers%20serializers.py.png)
- ![catscoffeecovers urls.py](/catscoffeecovers/urls.py)
- ![catscoffeecovers views.py](/catscoffeecovers/views.py)
- ![comments models.py](/comments/models.py)
- ![comments serializers.py](/images/comments%20serializers.py.png)
- ![comments urls.py](/images/comments%20urls.py.png)
- ![comments views.py](/images/comments%20views.py.png)
- ![followers models.py](/images/followers%20models.py.png)
- ![followers serializers.py](/images/followers%20serializers.py.png)
- ![followers urls.py](/images/followers%20urls.py.png)
- ![followers views.py](/images/followers%20views.py.png)
- ![profiles models.py](/images/profiles%20models.py.png)
- ![profiles serializers.py](/images/profiles%20serializers.py.png)
- ![profiles urls.py](/images/profiles%20urls.py.png)
- ![profiles views.py](/images/profiles%20views.py.png)

## Bugs

1. *Issue*
- A 'Forbidden 403' error was coming up when trying to access '/profiles. page even though correct address has been added to ALLOWED_HOSTS.
- *Solution*
- Added "CSRF_TRUSTED_ORIGINS = ['https://....'] " to settings.py
- ![bug screenshot](/images/bug.png)

2. *Issue* 
- After deploying the back-end of the project showed a 400 Error.
- *Solution*
- Upon searching for the solution online and discussion with my mentor, it was decided that it must be an issue with ALLOWED_HOST and/or DEBUG.I changed DEBUG to True and made sure that my ALLOWED_HOSTS were correct. I then realised that I had changed two variables so went back and changed DEBUG back to 'DEV' in os.environ and it still worked.
- ![bug screenshot](/images/bug4.png)

