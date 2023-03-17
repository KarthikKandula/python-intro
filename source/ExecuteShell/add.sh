#!/bin/bash

# Check if two arguments are provided
if [ $# -eq 2 ]; then
  # Assign the arguments to variables
  num1=$1
  num2=$2
  # Add the numbers and print the result
  result=$((num1 + num2))
  echo "The sum of $num1 and $num2 is $result"
  # Subtract the numbers and print the result
  result=$((num1 - num2))
  echo "The difference of $num1 and $num2 is $result"
  # Multiply the numbers and print the result
  result=$((num1 * num2))
  echo "The product of $num1 and $num2 is $result"
  # Divide the numbers and print the result
  result=$((num1 / num2))
  echo "The division of $num1 and $num2 is $result"
else
  # Print an error message if not enough arguments are provided
  echo "Please provide two numbers as arguments"
fi