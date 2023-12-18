#include <fstream>
#include <string>
#include <iostream>
int main() { # Open the input file
  std::ifstream inputFile("FahrenheitTemperature.txt");
  std::ofstream outputFile("CelsiusTemperature.txt");# Open the output file
  std::string cityName;
  int temperatureF;
  if (inputFile.is_open() && outputFile.is_open()) {#Check to see if the file opened successfully.
    while (inputFile >> cityName >> temperatureF) {
      int temperatureC = ((temperatureF - 32) * 5) / 9;#Convert Fahrenheit to Celsius using the formula.
      outputFile << cityName << " " << temperatureC << "\n";# City and its temperature in Celsius.
    }
    inputFile.close();# close both files input/output.
    outputFile.close();
    std::cout << "Conversion completed successfully.";
  } else {
    std::cout << "Unable to open file";
  }
  return 0;
}