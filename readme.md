# Description
This project is for creating file(s) that can be used to print out Data Machines property tag stickers. The file(s) created are word documents with images embedded in them. The images are align to print on Avery Label Sheets.

The project was later dockerized for easy usage. Instructions for using docker to generate Qr tags will be shown first, followed by the previous description and method of usage. 

## Usage with Docker-Compose
1. Download the docker.compose.yml file
2. Make the directory named "QrSheets" and "database" in the same directory as the docker-compose file
3. Run: dock-compose up

    This will do the following:
    - Generate 3 Sheets of Qr labels in the "QrSheets" directory.
    - Update the dmcProductList.db and place it in the "database" directory


4. _**Check in the dmcProductList.db**_ file every time a new set of stickers are created otherwise duplicate tags may be created.




## configuration
+ it is assume that the qrCfg.yaml config file is in the same directory that you are executing python code from
+ configuration elements:
1. qrDir: This is the directory that the code will use to place newly generated property tag images in (ex - './duoQr')
1. usedqrDir: This is the directory that the code will move images to once it has been used (ex - './usedDuoQr')
1. stickersPerPage: Leave at 32 unless you are using a different template file. This maches the number of stickers that are on a sheet
1. numDigits: The number of digits to that a property tag id should have (Leave as 6)
⋅⋅⋅The images has been size for 6 digits. The developer should resize the image if the number of digits are increase
1. db: The database that contains the list of all taking property tag ids (ex. - 'dmcProductList.db')
1. stickertemplate: The template file you will use to create an output file to print stickers with. Leave as is unless you get a diffrent template file from the vendor 
1. outputfiles: a list of output files to be created that will be used to print stickers with
⋅⋅⋅example:
⋅⋅⋅ - duoQrA1.docx
⋅⋅⋅ - duoQrA2.docx

## Requirements
1 - That the directories(qrDir and usedqrDir) reference in the config file already exists

## Usage:
python3 insQr2.py


## recommendations
the dmcProductList.db file should be check in every time a new set of stickers are created

## overview
### safeRandom
This code generates a random ID to be used for for creating an property tag image
The random Id is checked against an existing database of previous created id. This is done to prevent id collision.
Any random Id that this code returns will be also added to the database.
### gen2qr
This code uses safeRandom to get avaivable ids and creates an image with two property Id per image. This is done due to a request that we have smaller stickers. Instead of buying(and wasting existing label sheets), it was decided to have two images per sticker. The code will create the number of stickers that is requested and place them in a directory(this is the qrDir directory int he config file)
### insQr2
This code performs the following
1. Loads the config file
2. Creates an instance of safeRandom and shuts it down when done
3. Use gen2qr to create the property tag images that are needed
4. Take the generated images and insert them into a copy of the Avery word template document
5. Move used generated images to another directory when it is done
6. Save the update template document as a new file with name that has been

