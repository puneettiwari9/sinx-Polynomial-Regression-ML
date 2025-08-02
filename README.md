📐 Polynomial Regression Approximation of sin(x)
This project demonstrates how to approximate the sine function (sin(x)) using Polynomial Regression in Python. It fits a polynomial curve to given data points of sin(x) between 0 and 180 degrees, and allows the user to input custom angles to predict their sine values.

✨ Features
Trains a Polynomial Regression Model (Degree = 5) on sample sine values.

Generates a smooth curve approximating sin(x) from 0° to 180°.

Accepts user inputs (angle in degrees) and predicts sine values using the trained model.

Compares the predicted vs actual sine values.

🖼 Sample Output Graph


🛠 Requirements
Python 3.x

numpy

matplotlib

scikit-learn

Install via pip:
bash
Copy
Edit
pip install numpy matplotlib scikit-learn
🚀 Run Instructions
Clone this repository.

Ensure the image Figure_1.png is in the repository folder.

Run the Python script:

bash
Copy
Edit
python sin_polynomial_regression.py
The graph will display, and the console will prompt for 5 user inputs (in degrees).

📋 Example User Interaction
java
Copy
Edit
Attempt 1/5 - Enter a value of x (in degrees, between 0 and 180): 45
Predicted sin(45°) ≈ 0.70711
Actual sin(45°) = 0.70711

Attempt 2/5 - Enter a value of x (in degrees, between 0 and 180): 90
Predicted sin(90°) ≈ 1.00000
Actual sin(90°) = 1.00000
🧑‍💻 Author
Poornima Tiwari (BCA-NEW-33)

🌟 Tags:
#Python #MachineLearning #PolynomialRegression #sinxApproximation #ScikitLearn #MLProject

📁 Recommended GitHub Repository Structure:
bash
Copy
Edit
Polynomial-SinX-Approximation/
│
├── Figure_1.png              # Output Graph Image
├── sin_polynomial_regression.py  # Main Python Script
└── README.md                 # Project Documentation
