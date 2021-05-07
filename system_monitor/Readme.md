
##Local Environment Setup:

1. Create Virtual environment
   ```
    python3 -m venv venv
   ```
2. Activate Virtual environment

   For Linux:
   ```
   source venv/bin/activate
   ```
   For Windows
   ```
   venv\Scripts\activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. run server
   ```
    python server.py
   ...
   

About Metrics:----------

Metrics are useful because they provide insight into
the behavior and health of your systems, especially
when analyzed in aggregate. They represent the raw 
material used by your monitoring system to build a 
holistic view of your environment, automate responses
to changes, and alert human beings when required.
Metrics are the basic values used to understand 
historic trends, correlate diverse factors, and 
measure changes in your performance, consumption, or error rates.


While metrics represent the data in your system, monitoring is the process of collecting,
aggregating, and analyzing those values to improve awareness of your components’ characteristics and behavior. 
The data from various parts of your environment are collected into a monitoring system that is responsible for storage, 
aggregation, visualization, and initiating automated responses when the values meet specific requirements.

About Alerting:------

Alerting is the responsive component of a monitoring system that performs actions based on changes in metric values. 
Alerts definitions are composed of two components: a metrics-based condition or threshold, and 
an action to perform when the values fall outside of the acceptable conditions

About Threshold:------
Thresholding is a technique in OpenCV, which is the
assignment of pixel values in relation to the 
threshold value provided. In thresholding,each pixel value 
is compared with the threshold value. If the pixel 
value is smaller than the threshold, it is set to 0, 
otherwise, it is set to a maximum value (generally 255)