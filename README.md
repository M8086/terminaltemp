# terminaltemp
### A simple temperature reporting script, with a twist!

This python script fetches the current temperature from Dark Sky once you have provided your API key and latitude + longitude of your desired area.

It will then print the temperature as an integer

If you add the following code to your bash profile (```.bashrc``` on Fedora) you can get your current temperature by typing ```weather```

```bash
function weather { python ~/Documents/Python/weather/weather.py;}
export -f weather
```
Open a new shell and enjoy getting your current temperature fromn the comfort of your CLI!
