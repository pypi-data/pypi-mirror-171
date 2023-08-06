# python-logger
a simple python logger

# how to use

* ## downloading the logger and installing required libraries

1. install the colorama library
2. download the logger and add to your project
3. import the logger using `import logger`
* ## personalizing the logger

1. to toggle the logging of levels you can change the `logLevel` from true to false
2. if you want to color your output switch the `colorText` variable from false to true
3. to color the level identifier you can switch the `colorLevelText` variable from false to true
4. if you wish to change the default color of a level you can do that by altering the colour variables(warnColor, infoColor, debugColor, ect.) in the file
5. the logger executes the quit() function when a fatal is logged if you wish to switch that off you can switch the `quitWhenLogFatal` variable from true to false

* ## logging default levels

1. to log a warning use the `log_warning` function
2. to log an info message use the `log_info` function
3. to log a debug message use the `log_debug` function
4. to log an error use the `log_error` function
5. to log a fatal error use the `log_fatal` function

* ## adding additional levels

1. to add custom levels create an instance of the `CustomLogLevel` class, for this you need to provide a name, a color(optional), and is the level used for fatal errors(optional)
2. e.g. `CustomLevel = logger.CustomLogLevel("CUSTOM", Fore.GREEN, False)` NOTE: if you don't provide the `color` parameter it will be set to the default color of your IDE or console, if you don't provide the `isFatal` parameter it will be set to false
3. to log the custom level you can use the `log` method of the class e.g. `CustomLevel.log("custom message")`