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
## Feature Engineering
The data is aggregated into epochs of 30sec duration i.e, 300 readings are aggregated into 1-D array for each of the readings. We used the "mne" and "pyedflib" packages in python to extract the respective PSG and Hypnogram files in a CSV format.  
  
We aggregated the data in each of these CSVs to required format through spark. The spark code was run using spark-shell through local machines. The data frames once aggregated to the required format were saved into csv files again to be used to build input tensors for the deep learning models.  
  
The total number of datapoints available to build the model are 389052. The figure 2 above shows a distribution of these datapoints among different labels. “Sleep stage 2” dominates and there is significant imbalance amongst the other classes as well.
## Approach
Different neural netwrok architectures such as CNN, RNN and CRNNs have been explored to carry out the multi-class classification of sleep patterns. And for the performance metric, we chose to go ahead with F1-score, since accuracy would lead to misleading interpretations given the imabalance in the data which also gives us an idea of how good the precision and recall are, simultaneously avoiding the accuracy paradox.
## Experimental Setup
We used a train-test split of 70-30 to validate the trained models in order to evaluate the model performance. MNE and pyedflib readers were used in order to process the sleep telemetry electrophysiological EDF signal data. The data aggregation has been carried out in Spark, the data from which was used as the input for the modeling part of the project. The model has been run on Google Collaboratory in order to leverage the improved specs as compared to our personal systems. Through google colab, we used 26GB of RAM and the CPU specs are “Intel® Xeon® CPU @ 2.30GHz”.
## Results
A lot of iterations were tried out in every architecture and here we present the best iterations from each architecture and the final results.
### Baseline 1: CNN (1 channel):
For the first baseline, we used a single channel from the EEG Pz-Oz electrode as has been suggested to yield better classification performance than other channels in previous studies.  
We used two one-dimensional convolution layers:
  - The first layer with 1 input channel, 6 output channels with a kernel of size 5
  - The succeeding layer with 6 input channels, 16 output channels with a kernel size 5
  
Both the convolution layers were individually followed by a ReLU activation and a max pooling layer of size 2 with a dropout ratio of 0.2 followed by a hidden linear layer with 128 nodes followed by a ReLU activation and a dropout ratio of 0.2 and an output linear layer with 6 nodes.  
  
We also implemented early stopping in order to avoid overfitting with a patience of 20 epochs, the results of which can be seen below:  
![accuracy_curves (1)](https://user-images.githubusercontent.com/52098514/81035606-a8a02800-8e69-11ea-8dd7-42c0d0a79cf2.png)
![loss_curves (1)](https://user-images.githubusercontent.com/52098514/81035607-a8a02800-8e69-11ea-87b6-6d810bf21adb.png)
![normalized_confusion_matrix (1)](https://user-images.githubusercontent.com/52098514/81035597-a047ed00-8e69-11ea-81f3-0ac22daf38b1.png)  
F1-score: [0.80, 0.09, 0.74, 0.02, 0.61, 0.53]
The predictions for classes such as "Sleep stage 1" and Sleep stage 3" are significantly inaccurate as can be inferred from the F1-score and the confusion matrix. Going forward, we aim to improve upon this with the RNN and the CRNN architectures.
### Baseline 2: RNN (3 channels):
All 3 channels were used for the second baseline. As for the RNN architecture, we used a GRU layer with 16 hidden units and a dropout ratio of 0.2. In alignment with the data, we used 300 input channels with 3 layers. The GRU layer was followed by ReLU activation. The final output layer is a linear layer with 16 input features and 6 output features.  
![accuracy_curves (1)](https://user-images.githubusercontent.com/52098514/81036070-a939be00-8e6b-11ea-95dc-a965df266532.png)
![loss_curves (1)](https://user-images.githubusercontent.com/52098514/81036069-a939be00-8e6b-11ea-9b9b-13ceb8f035fa.png)
![normalized_confusion_matrix (1)](https://user-images.githubusercontent.com/52098514/81036059-9fb05600-8e6b-11ea-8ef6-cd9ceced5374.png)  
F1-score: [0.57, 0., 0.66, 0., 0.15, 0.33]  
This model clearly underperforms with a less than ~55% accuracy in comparison to the accuracy of CNN Baseline 1 with an accuracy of ~65% which is also evident from the F1 scores. The model does not overfit with the training accuracies being on par with the validation accuracies and early stopping has reached before 40 epochs.
### Final Model: CRNN (3 channels):
As for the CRNN models, multiple architectures were tried out including tuning hyperparameters such as batch size. Here, we present the final iteration which outperformed the rest of the models, the architecture of which is:
- The first layer with 3 input channels, 6 output channels with a kernel of size 5
- The second layer with 6 input channels, 16 output channels with a kernel of size 5  
  
Each of the convolution layers were followed by ReLU activation and a max pooling of size 2. This is followed by a linear transformation connected to a hidden layer with 128 nodes and then a GRU layer with a hidden size of 32, 5 layers and a dropout ratio of 0.2 connected linearly to the output layer with 6 nodes. The model has been implemented on 40 epochs and a batch size of 256.  

