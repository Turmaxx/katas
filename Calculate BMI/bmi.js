function bmi(weight, height){
    let index = weight / Math.pow(height, 2);


    if (index <= 18.5){
      return "Underweight";
    }
    else if (index <= 25.0){
      return "Normal";
    }
    else if (index <= 30.0){
      return "Overweight";
    }
    return "Obese";
}
    