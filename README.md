# Big Data in Healthcare - Sleep Stage Classification
A project that has been done as part of Georgia Tech coursework CSE 6250 - Big Data in Healthcare. The aim of the project is to accurately predict sleep stages corresponding to an individual's sleep cycle patterns thereby expediting the process of diagnosing sleep-related disorders.
## Introduction
Sleep patterns can be an important indicator of sleep apnea, insomnia, and risk of cardiovascular disorders. It, therefore, becomes important and beneficial to categorize sleep patterns. Classifying sleep patterns manually requires expert supervision and is time-consuming, subjective and expensive. So, as a part of this project we porposed to build a multi-class classifier that accurately labels sleep patterns.
## Data
The dataset chosen is the Sleep Telemetry EDF data from the PhysioNet database which contains 44 sleep recordings with corresponding manual labels developed by well-trained professionals. The sleep patterns are categorized into stages W, R, 1, 2, 3, 4, M (Movement time) and ? (not scored).
The 44 recordings were developed through 22 subjects (7 male and 15 female). The histogram showing the distribution of the age of the subjects is shown in Fig.1 below. About 54% of the subjects are in the age bracket 18-42.
![WhatsApp Image 2020-04-25 at 8 47 07 PM](https://user-images.githubusercontent.com/52098514/81017052-930e0c80-8e2f-11ea-86a9-e37be23cedbf.jpeg)
![WhatsApp Image 2020-04-25 at 8 48 11 PM](https://user-images.githubusercontent.com/52098514/81030814-2a875580-8e58-11ea-8e53-ed88f8efc207.jpeg)
As can be seen above, the data si from a total of 44 recordings corresponding to 22 subjects (7 male and 15 female) with the dominant age group being 18-30. And from the sleep stage frequency, we can say that there is significant class imbalance in our data. Out of the available channels, only EEG Fpz-Cz, EEG Pz-Oz and EOG horizontal were considered for the prediction purposes.
