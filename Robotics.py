#IMPORT SECTION
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import speech_recognition as sr
import pandas as pd
import serial 
import os
import time

#INTILIZATION SECTION
file_dir = "C:/Users/mexbow/data.csv"
file2_dir = "C:/Users/mexbow/Crop_recommendation.csv"
Moister_Dir = "C:/Users/mexbow/Desktop/ProjectBackups/MoistureData.text"
Temp_Dir = "C:/Users/mexbow/Desktop/ProjectBackups/TempData.text"
Hunidity_Dir = "C:/Users/mexbow/Desktop/ProjectBackups/HumidityData.text"
Rain_Dir = "C:/Users/mexbow/Desktop/ProjectBackups/RainData.text"
Ph_Dir = "C:/Users/mexbow/Desktop/ProjectBackups/PhData.text"
Temp_Data = None
Moister_Data = None
Ph_Data = None
Humidity_Data = None
Rain_Data = None
srl = serial.Serial("COM2",9600)

#FILE HANDLING SECTION
def SAVE_TEXT(filename, data):
    with open(filename, "a") as file:
        file.write(str(data) + "\n")

def DELETE_FILE(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

#TEXT RECOGNIZATION SECTION
def START():
    recognizer = sr.Recognizer()
    while True: 
        with sr.Microphone() as Mic:
            recognizer.adjust_for_ambient_noise(Mic,duration=0.2)
            srl.write(b'l')
            time.sleep(1)
            audio = recognizer.listen(Mic,phrase_time_limit=3)
            srl.write(b'c')
        try:
            srl.write(b'r')
            text = recognizer.recognize_google(audio)
            text.lower()       

            if "start" in text:
                srl.write(b's')
                break

            else:
                srl.write(b'w')
                time.sleep(12)

        except sr.UnknownValueError:
            srl.write(b'n')
            time.sleep(12)

        except sr.RequestError as e:
            srl.write(b'g')
            time.sleep(12)

#MODELS SECTION
def MODEL1(FD, moisture, temp):    
    data = pd.read_csv(FD)    
    test = data.drop(['crop'], axis=1)
    label_encoder = LabelEncoder()
    test['pump'] = label_encoder.fit_transform(test['pump'])
    X = test.drop(['pump'], axis=1)
    Y = test['pump']

    X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, Y_train)

    new_data = pd.DataFrame({
        'moisture': [moisture],
        'temp': [temp]
    })
    
    predictions = knn.predict(new_data)
    prediction = label_encoder.inverse_transform(predictions)

    for crop in prediction:
        if crop == 1:
            srl.write(b'O')
    
        else:
            srl.write(b'N')

def MODEL2(FD, temp, humidity, ph, rain):
    data = pd.read_csv(FD)
    test = data.drop(['N','P','K'],axis=1)
    label_encoder = LabelEncoder()
    test['label_encoded'] = label_encoder.fit_transform(test['label'])
    X = test.drop(['label', 'label_encoded'], axis=1)
    y = test['label_encoded']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    input_data = pd.DataFrame({
       'temperature': [temp],
       'humidity': [humidity],
       'ph': [ph],
       'rainfall': [rain]
    })

    predicted_crops = knn.predict(input_data)
    predicted_crop = label_encoder.inverse_transform(predicted_crops)
    crop = str(predicted_crop)
    chars_to_remove = "'[]"
    
    for char in chars_to_remove:
        crop = crop.replace(char, "")
    SAVE_TEXT("C:/Users/mexbow/Desktop/ProjectBackups/CropRec.text",crop)

#MAIN FUNCTION
def main():
    while True:
        task = srl.read()
        microphone = srl.read()
        
        if (task == b'1'):
            if (microphone == b'm') :
                global file_dir
                global Temp_Data
                global Moister_Data
                
                START()
                Model = srl.read()
                
                if (Model == b'M'):
                    with open(Temp_Dir, "r") as f:
                        Temp_Data = float(f.read().strip())
                    with open(Moister_Dir, "r") as f:
                        Moister_Data = float(f.read().strip())
                    DELETE_FILE(Moister_Dir)
                    DELETE_FILE(Temp_Dir)
                    MODEL1(file_dir,Moister_Data,Temp_Data)
                    break
        
        elif (microphone == b'm'):
            global file2_dir        
            Temp_Data
            global Ph_Data
            global Humidity_Data
            global Rain_Data
            
            START()
            Model = srl.read()
            
            if (Model == b'M'):
                with open(Temp_Dir, "r") as f:
                        Temp_Data = float(f.read().strip())
                with open(Hunidity_Dir, "r") as f:
                        Humidity_Data = float(f.read().strip())
                with open(Rain_Dir, "r") as f:
                    Rain_Data = float(f.read().strip())
                with open(Ph_Dir, "r") as f:
                    Ph_Data = float(f.read().strip())
                DELETE_FILE(Temp_Dir)
                DELETE_FILE(Hunidity_Dir)
                DELETE_FILE(Rain_Dir)
                DELETE_FILE(Ph_Dir)
                MODEL2(file2_dir,Temp_Data,Humidity_Data,Ph_Data,Rain_Data)
            
            break

if __name__ == '__main__':
    main()