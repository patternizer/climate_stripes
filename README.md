![image](https://github.com/patternizer/climate_stripes/blob/master/title_frame.png)

# climate_stripes

Python research code to visualise the data from a temperature monitoring station and is inspired by https://showyourstripes.info/ 
and based on the graphics of lead scientist: Professor Ed Hawkins and uses online data from Berkeley Earth: 
http://berkeleyearth.lbl.gov/stations/155170.
  
## Contents

* `climate_stripes.py` - main script to be run with Python 3.6+

The first step is to clone the latest climate_stripes code and step into the check out directory: 

    $ git clone https://github.com/patternizer/climate_stripes.git
    $ cd climate_stripes
    
### Using Standard Python 

The code should run with the [standard CPython](https://www.python.org/downloads/) installation and was tested 
in a conda virtual environment running a 64-bit version of Python 3.6+.

climate_stripes can be run from sources directly, once the following module requirements are resolved:

* `cottbus-berkley-earth.txt` - temperature moitoring station data from Berkeley Earth (http://berkeleyearth.lbl.gov/stations/155170)

Run with:

    $ python climate_stripes.py
        
## License

The code is distributed under terms and conditions of the Attribution 4.0 International (CC BY 4.0) license: 
https://creativecommons.org/licenses/by/4.0/ and is designed to visualise temperature monitoring station data
from Berkeley Earth: http://berkeleyearth.lbl.gov/stations/155170 and provide an implementation akin to
https://showyourstripes.info/ - graphics and lead scientist: Professor Ed Hawkins.

## Contact information

* [Michael Taylor](https://patternizer.github.io)
