# Automated de-identification of free-text electronic patient records (EPR)

Medical records are full of confidential and highly sensitive patient information, which are required
to be removed if they are to be used for secondary purposes beyond direct patient care.

This project aims to remove the following personal data from within patient records whilst
retaining the top level meaning of the redacted information.

__For example:__
<br>"Anthony suffers from Epilepsy."
<br>"\[Patient name\] suffers from Epilepsy."

## Personal information redacted

A brief overview of the categories of personal information redacted.

|Value|Description|
|---|---|
|Names||
|Date of Birth||
|Address||
|Contact details||
|Healthcare identifiers||
|||


## MedCAT

For further information on the MedCAT tool is available [here](https://github.com/CogStack/MedCAT).

## Building the MedCAT Model foundations

There are two essential components of the MedCAT model required for this project.

1) Vocab

2) Concept Database (CDB)

## Training the model

This base model is trained using the [MedCATtrainer](https://github.com/CogStack/MedCATtrainer) platform to annotate any 
identifiable information from Medical records.


