# Driver-Assistance-System
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/1.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/2.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/3.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/4.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/5.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/6.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/7.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/8.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/9.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/10.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/11.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/12.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/13.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/14.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/15.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/16.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/17.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/18.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/19.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/20.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/21.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/22.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/23.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/24.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/25.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/26.png)
![.](https://github.com/lycanthrope10100/Driver-Assistance-System/blob/master/Resources/27.png)

## Usage:
```cs
python drowsy.py --shape-predictor shape_predictor_68_face_landmarks.dat
python drowsy.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav
python drowsy.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav --webcam 0
```

## Debugging:
* If the eye aspect ratio is too low or too high, you may need to change this value
```cs
Line 53 - EYE_AR_THRESH = 0.3
```
* If the mouth aspect ratio is too low or too high, you may need to change this value
```cs
Line 55 - MOUTH_AR_THRESH = 0.65
```
