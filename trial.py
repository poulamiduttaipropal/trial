
#import urllib.request

from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
#print("timestamp =", timestamp)
#def dl_jpg(url,path):
#	path = 'http' + timestamp + '.jpg'
#	urllib.request.urlretrieve(url,path)
#url = 'https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F248797%2Fpexels-photo-248797.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&docid=ShwNVOdFBcmkxM&tbnid=8c_UAo3gH_220M%3A&vet=10ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ..i&w=500&h=200&client=ubuntu&bih=510&biw=1047&q=images&ved=0ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ&iact=mrc&uact=8'
#file_name = (url,'pics/')
#print('hello')

#import urllib.request

#from datetime import datetime

# current date and time
#now = datetime.now()

#timestamp = datetime.timestamp(now)
#print(timestamp)
#print("timestamp =", timestamp)
# url='https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F248797%2Fpexels-photo-248797.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&docid=ShwNVOdFBcmkxM&tbnid=8c_UAo3gH_220M%3A&vet=10ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ..i&w=500&h=200&client=ubuntu&bih=510&biw=1047&q=images&ved=0ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ&iact=mrc&uact=8'
# #url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F326055%2Fpexels-photo-326055.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&docid=ShwNVOdFBcmkxM&tbnid=Hc12q6ggbzStcM%3A&vet=10ahUKEwjqh46LqdTiAhUK6XMBHSI2DKsQMwh9KAIwAg..i&w=500&h=281&bih=949&biw=1920&q=images&ved=0ahUKEwjqh46LqdTiAhUK6XMBHSI2DKsQMwh9KAIwAg&iact=mrc&uact=8'
# file_name="hello"
# def dl_jpg(url,file_path,file_name):
# 	full_path ='http'+ file_name + '.jpg'
# 	urllib.request.urlretrieve(url,full_path)
# #url = 'https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F248797%2Fpexels-photo-248797.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&docid=ShwNVOdFBcmkxM&tbnid=8c_UAo3gH_220M%3A&vet=10ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ..i&w=500&h=200&client=ubuntu&bih=510&biw=1047&q=images&ved=0ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ&iact=mrc&uact=8'
# file_name = (url,'home/poulami/Pictures/',file_name)
# print('hello')
# import urllib.request
# import random
# def download_image(url,path):
#     name = random.randrange(1,100)
#     fullname = path + str(name)+".jpg"
#     urllib.request.urlretrieve(url,fullname)     
# download_image("https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F248797%2Fpexels-photo-248797.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&docid=ShwNVOdFBcmkxM&tbnid=8c_UAo3gH_220M%3A&vet=10ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ..i&w=500&h=200&client=ubuntu&bih=510&biw=1047&q=images&ved=0ahUKEwi53r_F6dLiAhVZ7HMBHXGMC9IQMwh9KAEwAQ&iact=mrc&uact=8","Pictures/")
import urllib.request
#import random
def download_image(url,path):
 #   name = random.randrange(1,100)
    fullname = path + str(timestamp) +".jpg"
    urllib.request.urlretrieve(url,fullname)     
download_image("https://www.google.com/imgres?imgurl=http%3A%2F%2Fpersonal.psu.edu%2Fxqz5228%2Fjpg.jpg&imgrefurl=http%3A%2F%2Fpersonal.psu.edu%2Fxqz5228%2Fjpg.html&docid=F0AM3uST3qogpM&tbnid=NfuDGtWEj8btoM%3A&vet=10ahUKEwieyNvY9d7iAhUg_XMBHYm6BxIQMwh9KAEwAQ..i&w=630&h=354&bih=900&biw=1920&q=jpg%20image&ved=0ahUKEwieyNvY9d7iAhUg_XMBHYm6BxIQMwh9KAEwAQ&iact=mrc&uact=8","pics/")

