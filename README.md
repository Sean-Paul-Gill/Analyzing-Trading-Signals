# Analyzing-Trading-Signals
This project is unorthodox. Market Data is collected and Signal Processing techniques are applied coincide with common Trading Methods to obtain beautiful results.

Please view the PDF file to view the entire project. All methods that were used were broken into the following format:
Theory, Implementation, Results and Conclusion

| Method | Functionality |
| --- | --- |
| Time/Frequency Analysis | Analysis of the Trading signal in the discrete-time domain and the frequency domain (magnitude & phase) |
| Windowing Methods | Changing the spectral properties (larger – subset) to obtain a greater insight to the signal in question |
| Savitzy-Golay Filter | A DSP technique for smoothing the data without distorting the signal tendency |
| Bollinger Bands | For Anomaly Detection. Tailoring the method using a combination of the Savitzty-Golay and current Bollinger strategy |
| Moving Average Filter | Taking the average of the previous n samples. Smoothes the sampled signal. |
| Average Anomaly Detection | Using the Moving Average Filter signal and statistics to draw conclusions on where anomalies have occured |
| Linear Predictive Algorithm | Obtaining the m linear co-efficients and predicting the next Trading value |
| Cross Correlation | Analyzing the correlation between certain markets using the DSP technique |
| Stochastic Indicator | Shows the momentum of the trade/signal by comparing the closing price with preivous trading ranges |
| Machine-Learning | Uisng common machine learning techniques on all the data generated from the techniques implemented |
