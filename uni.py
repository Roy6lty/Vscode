{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1c6d5ac7-d580-4093-a745-9cbccecf4550",
   "metadata": {},
   "source": [
    "# This is a object orented programing Doc"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2631758d-c029-4f34-b471-d86b2e26c035",
   "metadata": {},
   "source": [
    "#Class\n",
    "A class is a general existance of an entity in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4e255ca7-8a40-4ef2-9ce9-97f57626a723",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a Class\n",
    "class city:\n",
    "    def pop_density(self, a , b ):\n",
    "        return  a/b\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7d923bac-946e-47e5-b9ef-f02710319ed1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc418532-adc2-4c6c-a397-8e6f46e0b426",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A class has several Instances of an Object\n",
    "# City1 is an instance of the city Class\n",
    "# road, houses, name, pop, area, are attributes of city1\n",
    "city1 = city()\n",
    "city1.road = 500\n",
    "city1.houses = 10000\n",
    "city1.name = 'Warri'\n",
    "city1.pop = 60000 \n",
    "city1.area = 8000\n",
    "\n",
    "# \n",
    "#City 2 assigning a variable to a class defines an instance\n",
    "city2 = city()\n",
    "city2.road = 900\n",
    "city2.houses = 400000\n",
    "city2.name = 'Benin'\n",
    "city2.area = 90000\n",
    "city2.pop = 80000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53595f51-ff05-4a2e-97b5-7c1c3d08a470",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(type(city))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "200333f7-c20b-4a6e-81b1-7a0588cb28f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(type(city1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f8ecd72-e426-47bd-8da1-3604cdd8bd93",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "622db603-411c-4a0d-a67f-e16197eca73b",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(type(city1.road))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7c536e3-f664-4e4b-ae96-aedb2b8a7e4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "city1.road"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4daea84e-33d2-4930-a2d2-03d6a41b3e7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A class can contain methods accessable to the instances of that class\n",
    "k = city1.pop_density(city1.area, city1.pop)\n",
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f015f172-39dc-404b-8db6-a82719e126d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "city1.pop/city1.area"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce859198-de3e-4df7-b8b3-7b6b1249b800",
   "metadata": {},
   "outputs": [],
   "source": [
    "# \n",
    "G = city2.pop_density(city2.area, city2.pop)\n",
    "print(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93347acd-41f2-4664-91cf-e6d2bdb1b532",
   "metadata": {},
   "source": [
    "# Version 1.01 \n",
    "Instances can be intialized with Attributes on creation\n",
    "This ensures certain attributes are intialzed with the creation of an instance\n",
    "helping in the prevention of error and for better code management\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "43c3cbc6-005e-4301-98c6-830167903d9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Fav']\n",
      "['Fieldcrest']\n",
      "[\"Saint Mary's\"]\n",
      "['Olufi_High_school']\n",
      "['Creedford']\n"
     ]
    }
   ],
   "source": [
    "#Instances of a Class are objects of that class each objrct has access to global variables within the class\n",
    "\n",
    "class school:\n",
    "    \n",
    "    schoolfees = 0.3142 #schoolfees is a class level variable \n",
    "    \n",
    "# the __init__ function is an inbuilt special function that initialzes when a class instance is created\n",
    "#-- certain attributes can be optional on a instance by intializing it to zero\n",
    "# each value datatype can be included \n",
    "\n",
    "    all =[] # a list for alll instances created in a class\n",
    "     \n",
    "    def __init__ (self, name: str, location: str, population: int, age: int, eff = 0):\n",
    "    # using the assert keyword to restrict the values that can be\n",
    "    #inputed into each instace\n",
    "    \n",
    "    # Run validations to recived Arguments and errors \n",
    "    \n",
    "    \n",
    "        assert age >= 0, f'The age {age} cannot be less than 0'                      # The age cannot be less than 0\n",
    "        assert population >= 0, f'The population {population} cannot be less than 0'  # The population cannot be less than 0\n",
    "    \n",
    "    # Assign to self objects instance attributes\n",
    "        self.name = name\n",
    "        self.location = location\n",
    "        self.population = population\n",
    "        self.age = age\n",
    "        \n",
    "        # Adding instances to the list wit the class \n",
    "        school.all.append(self) # The school class adds all instances of itself to the list\n",
    "        \n",
    "        \n",
    "    def rating(self, a, b):\n",
    "        return a/b\n",
    "    \n",
    "# the rating1 mrthod uses the intialzed insstances\n",
    "    def rating1(self):\n",
    "        return self.population/self.age\n",
    "    def schfees(self):\n",
    "        return (school.schoolfees) * (self.population)\n",
    "    # each instance of school is an Object to rename that object we use the special method __repr__\n",
    "    def __repr__(self):\n",
    "        return f\"school1 has ('{self.name,},{self.location},{self.population},{self.age})\"\n",
    "\n",
    "    \n",
    "# creating a class instance for the class school\n",
    "school1 = school('Fav', 'Osun state', 347, 2)\n",
    "school2 = school('Fieldcrest', 'Delta state', 609, 8)\n",
    "school3 = school(\"Saint Mary's\", 'Edo', 458, 12)\n",
    "school4 = school(\"Olufi_High_school\", 'Ondo State',350 , 21)\n",
    "school5 = school('Creedford', 'Rivers state', 233, 4)\n",
    "\n",
    "# -- other attribute can also be assigned manually to the class instance \n",
    "school1.field = True\n",
    "for i in school.all:\n",
    "    print(i.name.split(','))\n",
    "        \n",
    "#schools = { 'Names' : []}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "88433540-7377-4315-a9fb-4f1c90f3440b",
   "metadata": {},
   "outputs": [
    {
     "ename": "PermissionError",
     "evalue": "[Errno 13] Permission denied: 'C:/Users/hp/Downloads/Documents/schools.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mPermissionError\u001b[0m                           Traceback (most recent call last)",
      "Input \u001b[1;32mIn [86]\u001b[0m, in \u001b[0;36m<cell line: 7>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m schools \u001b[38;5;241m=\u001b[39m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mName\u001b[39m\u001b[38;5;124m'\u001b[39m : [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mFavour\u001b[39m\u001b[38;5;124m'\u001b[39m ,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mFieldcrest\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSaint Mary\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124ms\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOlufi_High_school\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mCreedford\u001b[39m\u001b[38;5;124m'\u001b[39m],\n\u001b[0;32m      2\u001b[0m             \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mState\u001b[39m\u001b[38;5;124m'\u001b[39m : [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOsun state\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDelta state\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mEdo state\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mOndo state\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRivers state\u001b[39m\u001b[38;5;124m'\u001b[39m],\n\u001b[0;32m      3\u001b[0m            \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mPopulation\u001b[39m\u001b[38;5;124m'\u001b[39m: [\u001b[38;5;241m347\u001b[39m, \u001b[38;5;241m609\u001b[39m, \u001b[38;5;241m458\u001b[39m, \u001b[38;5;241m350\u001b[39m, \u001b[38;5;241m233\u001b[39m],\n\u001b[0;32m      4\u001b[0m            \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mage\u001b[39m\u001b[38;5;124m'\u001b[39m : [\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m8\u001b[39m,\u001b[38;5;241m12\u001b[39m,\u001b[38;5;241m21\u001b[39m,\u001b[38;5;241m4\u001b[39m]\n\u001b[0;32m      5\u001b[0m           }\n\u001b[0;32m      6\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mDataFrame(schools)\n\u001b[1;32m----> 7\u001b[0m \u001b[43mdf\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mC:/Users/hp/Downloads/Documents/schools.csv\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:3551\u001b[0m, in \u001b[0;36mNDFrame.to_csv\u001b[1;34m(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, line_terminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options)\u001b[0m\n\u001b[0;32m   3540\u001b[0m df \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m, ABCDataFrame) \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mto_frame()\n\u001b[0;32m   3542\u001b[0m formatter \u001b[38;5;241m=\u001b[39m DataFrameFormatter(\n\u001b[0;32m   3543\u001b[0m     frame\u001b[38;5;241m=\u001b[39mdf,\n\u001b[0;32m   3544\u001b[0m     header\u001b[38;5;241m=\u001b[39mheader,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   3548\u001b[0m     decimal\u001b[38;5;241m=\u001b[39mdecimal,\n\u001b[0;32m   3549\u001b[0m )\n\u001b[1;32m-> 3551\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mDataFrameRenderer\u001b[49m\u001b[43m(\u001b[49m\u001b[43mformatter\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   3552\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpath_or_buf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3553\u001b[0m \u001b[43m    \u001b[49m\u001b[43mline_terminator\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mline_terminator\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3554\u001b[0m \u001b[43m    \u001b[49m\u001b[43msep\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43msep\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3555\u001b[0m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3556\u001b[0m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3557\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3558\u001b[0m \u001b[43m    \u001b[49m\u001b[43mquoting\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquoting\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3559\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcolumns\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcolumns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3560\u001b[0m \u001b[43m    \u001b[49m\u001b[43mindex_label\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mindex_label\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3561\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3562\u001b[0m \u001b[43m    \u001b[49m\u001b[43mchunksize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mchunksize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3563\u001b[0m \u001b[43m    \u001b[49m\u001b[43mquotechar\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquotechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3564\u001b[0m \u001b[43m    \u001b[49m\u001b[43mdate_format\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mdate_format\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3565\u001b[0m \u001b[43m    \u001b[49m\u001b[43mdoublequote\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mdoublequote\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3566\u001b[0m \u001b[43m    \u001b[49m\u001b[43mescapechar\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mescapechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3567\u001b[0m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   3568\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\formats\\format.py:1180\u001b[0m, in \u001b[0;36mDataFrameRenderer.to_csv\u001b[1;34m(self, path_or_buf, encoding, sep, columns, index_label, mode, compression, quoting, quotechar, line_terminator, chunksize, date_format, doublequote, escapechar, errors, storage_options)\u001b[0m\n\u001b[0;32m   1159\u001b[0m     created_buffer \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m   1161\u001b[0m csv_formatter \u001b[38;5;241m=\u001b[39m CSVFormatter(\n\u001b[0;32m   1162\u001b[0m     path_or_buf\u001b[38;5;241m=\u001b[39mpath_or_buf,\n\u001b[0;32m   1163\u001b[0m     line_terminator\u001b[38;5;241m=\u001b[39mline_terminator,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1178\u001b[0m     formatter\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mfmt,\n\u001b[0;32m   1179\u001b[0m )\n\u001b[1;32m-> 1180\u001b[0m \u001b[43mcsv_formatter\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msave\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1182\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m created_buffer:\n\u001b[0;32m   1183\u001b[0m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(path_or_buf, StringIO)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\formats\\csvs.py:241\u001b[0m, in \u001b[0;36mCSVFormatter.save\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    237\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    238\u001b[0m \u001b[38;5;124;03mCreate the writer & save.\u001b[39;00m\n\u001b[0;32m    239\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    240\u001b[0m \u001b[38;5;66;03m# apply compression and byte/text conversion\u001b[39;00m\n\u001b[1;32m--> 241\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    242\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    243\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    244\u001b[0m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    245\u001b[0m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    246\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    247\u001b[0m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    248\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m handles:\n\u001b[0;32m    249\u001b[0m \n\u001b[0;32m    250\u001b[0m     \u001b[38;5;66;03m# Note: self.encoding is irrelevant here\u001b[39;00m\n\u001b[0;32m    251\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mwriter \u001b[38;5;241m=\u001b[39m csvlib\u001b[38;5;241m.\u001b[39mwriter(\n\u001b[0;32m    252\u001b[0m         handles\u001b[38;5;241m.\u001b[39mhandle,\n\u001b[0;32m    253\u001b[0m         lineterminator\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mline_terminator,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    258\u001b[0m         quotechar\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mquotechar,\n\u001b[0;32m    259\u001b[0m     )\n\u001b[0;32m    261\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_save()\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\common.py:789\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    784\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    785\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    786\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    787\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    788\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 789\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[0;32m    790\u001b[0m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    791\u001b[0m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    792\u001b[0m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    793\u001b[0m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    794\u001b[0m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[0;32m    795\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    796\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    797\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    798\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mPermissionError\u001b[0m: [Errno 13] Permission denied: 'C:/Users/hp/Downloads/Documents/schools.csv'"
     ]
    }
   ],
   "source": [
    "schools = {'Name' : ['Favour' ,'Fieldcrest', \"Saint Mary's\", 'Olufi_High_school', 'Creedford'],\n",
    "            'State' : ['Osun state', 'Delta state', 'Edo state', 'Ondo state', 'Rivers state'],\n",
    "           'Population': [347, 609, 458, 350, 233],\n",
    "           'age' : [2,8,12,21,4]\n",
    "          }\n",
    "df = pd.DataFrame(schools)\n",
    "df.to_csv(\"C:/Users/hp/Downloads/Documents/schools.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba2553fd-c4d8-44fc-bb07-e460a4018ab1",
   "metadata": {},
   "outputs": [],
   "source": [
    "school1.rating(school1.population, school1.age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80d4fdd2-d5c7-4dbe-9a9c-0e64492ad7ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# an empty method contains the self variable\n",
    "# Each instance usning the rating1 method\n",
    "print(school1.rating1())\n",
    "print(school2.rating1())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d586f2b3-be77-4506-9bf1-e90fabda30ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "# the instace has access to the class variable\n",
    "print(school1.schfees())\n",
    "print(school2.schfees())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67e282d1-8ed7-40fc-909a-86582406817f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# you can check the attributes on instances on a class level and instance level (__dict__)\n",
    "school.__dict__\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cad5d6af-b28a-4010-94bc-473c2549115b",
   "metadata": {},
   "outputs": [],
   "source": [
    "school1.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d58e53ec-9744-4043-90ad-fd32f51a3f97",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "75047679-50bc-4d68-960d-454b4b1488bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[school1 has ('('Favour',),Osun state,347,2),\n",
       " school1 has ('('Fieldcrest',),Delta state,609,8),\n",
       " school1 has ('(\"Saint Mary's\",),Edo,458,12),\n",
       " school1 has ('('Olufi_High_school',),Ondo State,350,21),\n",
       " school1 has ('('Creedford',),Rivers state,233,4)]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "school.all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "87b38913-a261-4333-a6e4-d3a8008b4986",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>State</th>\n",
       "      <th>Population</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Favour</td>\n",
       "      <td>Osun state</td>\n",
       "      <td>347</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fieldcrest</td>\n",
       "      <td>Delat state</td>\n",
       "      <td>609</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Saint Mary's</td>\n",
       "      <td>Edo state</td>\n",
       "      <td>458</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Olufi_High_school</td>\n",
       "      <td>Ondo state</td>\n",
       "      <td>350</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Creedford</td>\n",
       "      <td>Rivers state</td>\n",
       "      <td>233</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Name         State  Population  age\n",
       "0             Favour    Osun state         347    2\n",
       "1         Fieldcrest   Delat state         609    8\n",
       "2       Saint Mary's     Edo state         458   12\n",
       "3  Olufi_High_school    Ondo state         350   21\n",
       "4          Creedford  Rivers state         233    4"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2384953-768b-45f9-b96d-54c8b50f0363",
   "metadata": {},
   "source": [
    "# Version 1.02\n",
    "This version involves the instaiation of variables from a csv list automatically and also inputiing their properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "47a30949-add4-459e-92fe-7567a7a94879",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Instances of a Class are objects of that class each objrct has access to global variables within the class\n",
    "\n",
    "class school:\n",
    "    \n",
    "    schoolfees = 0.3142 #schoolfees is a class level variable \n",
    "    \n",
    "# the __init__ function is an inbuilt special function that initialzes when a class instance is created\n",
    "#-- certain attributes can be optional on a instance by intializing it to zero\n",
    "# each value datatype can be included \n",
    "\n",
    "    all =[] # a list for alll instances created in a class\n",
    "     \n",
    "    def __init__ (self, name: str, location: str, population: int, age: int, rank : int):\n",
    "    # using the assert keyword to restrict the values that can be\n",
    "    #inputed into each instace\n",
    "    \n",
    "    # Run validations to recived Arguments and errors \n",
    "    \n",
    "    \n",
    "        assert age >= 0, f'The age {age} cannot be less than 0'                      # The age cannot be less than 0\n",
    "        assert population >= 0, f'The population {population} cannot be less than 0'  # The population cannot be less than 0\n",
    "    \n",
    "    # Assign to self objects instance attributes\n",
    "        self.name = name\n",
    "        self.location = location\n",
    "        self.population = population\n",
    "        self.age = age\n",
    "        self.rank = rank\n",
    "        \n",
    "        # Adding instances to the list wit the class \n",
    "        school.all.append(self) # The school class adds all instances of itself to the list\n",
    "        \n",
    "        \n",
    "    def rating(self, a, b):\n",
    "        return a/b\n",
    "    \n",
    "\n",
    "    # the rating1 mrthod uses the intialzed insstances\n",
    "    def rating1(self):\n",
    "        return self.population/self.age\n",
    "    \n",
    "    def schfees(self):\n",
    "        return (school.schoolfees) * (self.population)\n",
    "   \n",
    "    # each instance of school is an Object to rename that object we use the special method __repr__\n",
    "    def __repr__(self):\n",
    "        return f\"school1 has ('{self.name,},{self.location},{self.population},{self.age})\"\n",
    "    \n",
    "    # Each method from a csv file is instatiated to create an object with the required properties\n",
    "    \n",
    "    # Creating a class method  i.e this method can only be accessed by the class itself not its instances\n",
    "    @classmethod\n",
    "    def instantiate_from_csv(cls):#cls means class, te class method can call itself and also use self but this wil be confusing \n",
    "        with open(\"C:/Users/hp/Downloads/Documents/Book1.csv\", 'r') as f:  #'F' is the variable holding the csv \n",
    "            reader = csv.DictReader(f)\n",
    "            schools = list(reader)\n",
    "            print(f)\n",
    "        for i in schools:\n",
    "            print(i)\n",
    "        for i in schools:\n",
    "            school(\n",
    "               rank = int(i.get('Rank')),\n",
    "               name = str(i.get('name')),\n",
    "               location = str(i.get('state')),\n",
    "               population = int(i.get('Population')),\n",
    "               age = int(i.get('age'))      \n",
    "             )\n",
    "     #Creating a staticMethod \n",
    "    @staticmethod\n",
    "    def is_integer(num):\n",
    "            if isinstance(num, float):\n",
    "                print(num.is_integer)\n",
    "                return num.is_integer()\n",
    "            elif isinstance(num, int):\n",
    "                return True\n",
    "            else:\n",
    "                return False\n",
    "            \n",
    "            \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "6e0890fe-e4b7-4643-a623-5c888646b164",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'rank' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [73]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mrank\u001b[49m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'rank' is not defined"
     ]
    }
   ],
   "source": [
    "rank"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4dc207ef-2ec0-4f1e-8e4b-5bbe0476ebe0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "daa38308-c599-46bc-836a-b569b6f28496",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='C:/Users/hp/Downloads/Documents/Book1.csv' mode='r' encoding='cp1252'>\n",
      "{'Rank': '1', 'Name': 'University of Lagos', 'state': 'Lagos ...', 'Population': '13452', 'age': '42'}\n",
      "{'Rank': '2', 'Name': 'University of Nigeria', 'state': 'Nsukka ...', 'Population': '1075', 'age': '15'}\n",
      "{'Rank': '3', 'Name': 'University of Ibadan', 'state': 'Ibadan', 'Population': '6515', 'age': '20'}\n",
      "{'Rank': '4', 'Name': 'Obafemi Awolowo University', 'state': 'Ile-Ife', 'Population': '7683', 'age': '23'}\n",
      "{'Rank': '5', 'Name': 'University of Port Harcourt', 'state': 'Port Harcourt', 'Population': '3491', 'age': '12'}\n",
      "{'Rank': '6', 'Name': 'University of Ilorin', 'state': 'Ilorin', 'Population': '9880', 'age': '13'}\n",
      "{'Rank': '7', 'Name': 'Covenant University', 'state': 'Ota', 'Population': '4825', 'age': '60'}\n",
      "{'Rank': '8', 'Name': 'Ahmadu Bello University', 'state': 'Zaria', 'Population': '3330', 'age': '17'}\n",
      "{'Rank': '9', 'Name': 'Federal University of Technology, Akure', 'state': 'Akure', 'Population': '2431', 'age': '12'}\n",
      "{'Rank': '10', 'Name': 'Rivers State University', 'state': 'Port Harcourt', 'Population': '6197', 'age': '17'}\n",
      "{'Rank': '11', 'Name': 'Adekunle Ajasin University', 'state': 'Akungba Akoko ...', 'Population': '724', 'age': '41'}\n",
      "{'Rank': '12', 'Name': 'Federal University of Agriculture, Abeokuta', 'state': 'Abeokuta ...', 'Population': '9145', 'age': '17'}\n",
      "{'Rank': '13', 'Name': 'Landmark University', 'state': 'Omu-Aran', 'Population': '6618', 'age': '22'}\n",
      "{'Rank': '14', 'Name': 'Afe Babalola University', 'state': 'Ado-Ekiti', 'Population': '5338', 'age': '2'}\n",
      "{'Rank': '15', 'Name': 'University of Benin', 'state': 'Benin City', 'Population': '9527', 'age': '63'}\n",
      "{'Rank': '16', 'Name': 'American University of Nigeria', 'state': 'Yola', 'Population': '441', 'age': '22'}\n",
      "{'Rank': '17', 'Name': 'Taraba State University', 'state': 'Jalingo', 'Population': '1365', 'age': '45'}\n",
      "{'Rank': '18', 'Name': 'Ladoke Akintola University of Technology', 'state': 'Ogbomoso ...', 'Population': '2617', 'age': '11'}\n",
      "{'Rank': '19', 'Name': 'Bayero University Kano', 'state': 'Kano', 'Population': '6545', 'age': '18'}\n",
      "{'Rank': '20', 'Name': 'University of Jos', 'state': 'Jos', 'Population': '2530', 'age': '20'}\n",
      "{'Rank': '21', 'Name': 'University of Abuja', 'state': 'Abuja', 'Population': '1983', 'age': '30'}\n",
      "{'Rank': '22', 'Name': 'Babcock University', 'state': 'Ilishan-Remo ...', 'Population': '3345', 'age': '20'}\n",
      "{'Rank': '23', 'Name': 'Nile University of Nigeria', 'state': 'Abuja', 'Population': '7091', 'age': '16'}\n",
      "{'Rank': '24', 'Name': 'Federal University of Technology, Owerri', 'state': 'Owerri', 'Population': '725', 'age': '14'}\n",
      "{'Rank': '25', 'Name': 'Pan-Atlantic University', 'state': 'Lagos', 'Population': '3784', 'age': '18'}\n",
      "{'Rank': '26', 'Name': 'Nnamdi Azikiwe University', 'state': 'Awka ...', 'Population': '2835', 'age': '17'}\n",
      "{'Rank': '27', 'Name': 'Federal University, Oye-Ekiti', 'state': 'Oye-Ekiti ...', 'Population': '6477', 'age': '2022'}\n",
      "{'Rank': '28', 'Name': 'Veritas University', 'state': 'Abuja', 'Population': '339', 'age': '66'}\n",
      "{'Rank': '29', 'Name': 'Lagos State University', 'state': 'Ojo', 'Population': '2083', 'age': '20'}\n",
      "{'Rank': '30', 'Name': 'Baze University', 'state': 'Abuja', 'Population': '6401', 'age': '17'}\n",
      "{'Rank': '31', 'Name': 'University of Uyo', 'state': 'Uyo', 'Population': '16', 'age': '17'}\n",
      "{'Rank': '32', 'Name': 'Federal University of Technology, Minna', 'state': 'Minna ...', 'Population': '6684', 'age': '17'}\n",
      "{'Rank': '33', 'Name': 'Usmanu Danfodio University', 'state': 'Sokoto', 'Population': '2191', 'age': '20'}\n",
      "{'Rank': '34', 'Name': 'Federal University, Lokoja', 'state': 'Lokoja', 'Population': '9353', 'age': '1'}\n",
      "{'Rank': '35', 'Name': 'African University of Science and Technology', 'state': 'Abuja', 'Population': '3020', 'age': '30'}\n",
      "{'Rank': '36', 'Name': 'Olabisi Onabanjo University', 'state': 'Ago Iwoye ...', 'Population': '5072', 'age': '1'}\n",
      "{'Rank': '37', 'Name': 'Ebonyi State University', 'state': 'Abakaliki', 'Population': '9420', 'age': '26'}\n",
      "{'Rank': '38', 'Name': 'Ekiti State University, Ado Ekiti', 'state': 'Ado-Ekiti', 'Population': '7005', 'age': '17'}\n",
      "{'Rank': '39', 'Name': \"Redeemer's University\", 'state': 'Ede ...', 'Population': '803', 'age': '6'}\n",
      "{'Rank': '40', 'Name': 'Federal University, Otuoke', 'state': 'Otuoke', 'Population': '816', 'age': '10'}\n",
      "{'Rank': '41', 'Name': 'Benue State University', 'state': 'Makurdi', 'Population': '9083', 'age': '10'}\n",
      "{'Rank': '42', 'Name': 'Nasarawa State University', 'state': 'Keffi', 'Population': '4670', 'age': '11'}\n",
      "{'Rank': '43', 'Name': 'University of Calabar', 'state': 'Calabar', 'Population': '8675', 'age': '34'}\n",
      "{'Rank': '44', 'Name': 'Tai Solarin University of Education', 'state': 'Ijebu-Ode ...', 'Population': '9229', 'age': '41'}\n",
      "{'Rank': '45', 'Name': 'University of Maiduguri', 'state': 'Maiduguri', 'Population': '6493', 'age': '41'}\n",
      "{'Rank': '46', 'Name': 'Osun State University', 'state': 'Oshogbo ...', 'Population': '7659', 'age': '11'}\n",
      "{'Rank': '47', 'Name': 'Kwara State University', 'state': 'Ilorin', 'Population': '1950', 'age': '9'}\n",
      "{'Rank': '48', 'Name': 'Bowen University', 'state': 'Iwo', 'Population': '5623', 'age': '15'}\n",
      "{'Rank': '49', 'Name': 'Abubakar Tafawa Balewa University', 'state': 'Bauchi', 'Population': '6962', 'age': '13'}\n",
      "{'Rank': '50', 'Name': \"Umaru Musa Yar'Adua University\", 'state': 'Katsina', 'Population': '1285', 'age': '10'}\n",
      "{'Rank': '51', 'Name': 'Skyline University Nigeria', 'state': 'Kano', 'Population': '5941', 'age': '23'}\n",
      "{'Rank': '52', 'Name': 'Federal University, Dutsin-Ma', 'state': 'Dutsin-Ma', 'Population': '5310', 'age': '5'}\n",
      "{'Rank': '53', 'Name': 'Kaduna State University', 'state': 'Kaduna', 'Population': '5802', 'age': '16'}\n",
      "{'Rank': '54', 'Name': 'Abia State University', 'state': 'Uturu', 'Population': '861', 'age': '7'}\n",
      "{'Rank': '55', 'Name': 'Delta State University, Abraka', 'state': 'Abraka', 'Population': '5959', 'age': '7'}\n",
      "{'Rank': '56', 'Name': 'Enugu State University of Science and Technology', 'state': 'Enugu', 'Population': '3603', 'age': '39'}\n",
      "{'Rank': '57', 'Name': 'Mountain Top University', 'state': 'Makogi Oba', 'Population': '8327', 'age': '11'}\n",
      "{'Rank': '58', 'Name': 'Federal University, Lafia', 'state': 'Lafia', 'Population': '1699', 'age': '1'}\n",
      "{'Rank': '59', 'Name': 'Michael Okpara University of Agriculture', 'state': 'Umuahia', 'Population': '7318', 'age': '7'}\n",
      "{'Rank': '60', 'Name': 'Alex Ekwueme Federal University, Ndufu-Alike', 'state': 'Ikwo', 'Population': '5814', 'age': '21'}\n",
      "{'Rank': '61', 'Name': 'Lead City University', 'state': 'Ibadan', 'Population': '9848', 'age': '39'}\n",
      "{'Rank': '62', 'Name': 'Cross River University of Technology', 'state': 'Calabar ...', 'Population': '9112', 'age': '13'}\n",
      "{'Rank': '63', 'Name': 'Chukwuemeka Odumegwu Ojukwu University', 'state': 'Uli ...', 'Population': '5330', 'age': '30'}\n",
      "{'Rank': '64', 'Name': 'Akwa Ibom State University', 'state': 'Ikot Akpad ...', 'Population': '7257', 'age': '61'}\n",
      "{'Rank': '65', 'Name': 'University of Agriculture, Makurdi', 'state': 'Makurdi', 'Population': '5678', 'age': '13'}\n",
      "{'Rank': '66', 'Name': 'Godfrey Okoye University', 'state': 'Ugwuomu-Nike ...', 'Population': '8412', 'age': '17'}\n",
      "{'Rank': '67', 'Name': 'Federal University, Dutse', 'state': 'Dutse', 'Population': '5307', 'age': '17'}\n",
      "{'Rank': '68', 'Name': 'Edo University', 'state': 'Iyamho', 'Population': '3243', 'age': '4'}\n",
      "{'Rank': '69', 'Name': 'Al-Hikmah University', 'state': 'Ilorin ...', 'Population': '1130', 'age': '11'}\n",
      "{'Rank': '70', 'Name': 'Yusuf Maitama Sule University Kano', 'state': 'Kano', 'Population': '4912', 'age': '16'}\n",
      "{'Rank': '71', 'Name': 'Ambrose Alli University', 'state': 'Ekpoma', 'Population': '2562', 'age': '52'}\n",
      "{'Rank': '72', 'Name': 'Igbinedion University Okada', 'state': 'Okada ...', 'Population': '9084', 'age': '47'}\n",
      "{'Rank': '73', 'Name': 'Federal University of Petroleum Resources', 'state': 'Effurun', 'Population': '1516', 'age': '1'}\n",
      "{'Rank': '74', 'Name': 'Crawford University', 'state': 'Faith City ...', 'Population': '3924', 'age': '74'}\n",
      "{'Rank': '75', 'Name': 'University of Medical Sciences', 'state': 'Ondo City', 'Population': '2407', 'age': '51'}\n",
      "{'Rank': '76', 'Name': 'Imo State University', 'state': 'Owerri', 'Population': '95', 'age': '60'}\n",
      "{'Rank': '77', 'Name': 'Niger Delta University', 'state': 'Wilberforce Island', 'Population': '2148', 'age': '67'}\n",
      "{'Rank': '78', 'Name': 'Bells University of Technology', 'state': 'Ota', 'Population': '761', 'age': '47'}\n",
      "{'Rank': '79', 'Name': 'Benson Idahosa University', 'state': 'Benin City', 'Population': '155', 'age': '15'}\n",
      "{'Rank': '80', 'Name': 'Kogi State University', 'state': 'Anyigba', 'Population': '1586', 'age': '3'}\n",
      "{'Rank': '81', 'Name': 'Adeleke University', 'state': 'Ede', 'Population': '8340', 'age': '42'}\n",
      "{'Rank': '82', 'Name': 'Ajayi Crowther University', 'state': 'Oyo Town', 'Population': '735', 'age': '15'}\n",
      "{'Rank': '83', 'Name': 'Ibrahim Badamasi Babangida University', 'state': 'Lapai', 'Population': '1118', 'age': '20'}\n",
      "{'Rank': '84', 'Name': 'Elizade University', 'state': 'Ilara-Mokin', 'Population': '8871', 'age': '23'}\n",
      "{'Rank': '85', 'Name': 'Southwestern University, Nigeria', 'state': 'Okun Owa', 'Population': '5403', 'age': '12'}\n",
      "{'Rank': '86', 'Name': 'Chrisland University', 'state': 'Abeokuta', 'Population': '9158', 'age': '13'}\n",
      "{'Rank': '87', 'Name': 'Caleb University', 'state': 'Imota', 'Population': '609', 'age': '60'}\n",
      "{'Rank': '88', 'Name': 'Joseph Ayo Babalola University', 'state': 'Ikeji-Arakeji', 'Population': '7261', 'age': '17'}\n",
      "{'Rank': '89', 'Name': 'Bingham University', 'state': 'Auta Balifi', 'Population': '8650', 'age': '12'}\n",
      "{'Rank': '90', 'Name': 'Fountain University, Osogbo', 'state': 'Oshogbo', 'Population': '1344', 'age': '17'}\n",
      "{'Rank': '91', 'Name': 'Kola Daisi University', 'state': 'Ibadan', 'Population': '3941', 'age': '41'}\n",
      "{'Rank': '92', 'Name': 'Achievers University, Owo', 'state': 'Owo', 'Population': '2070', 'age': '17'}\n",
      "{'Rank': '93', 'Name': 'Yobe State University', 'state': 'Damaturu', 'Population': '3394', 'age': '22'}\n",
      "{'Rank': '94', 'Name': 'Kano University of Science and Technology', 'state': 'Wudil', 'Population': '2605', 'age': '2'}\n",
      "{'Rank': '95', 'Name': 'Federal University, Birnin Kebbi', 'state': 'Birnin Kebbi', 'Population': '6425', 'age': '63'}\n",
      "{'Rank': '96', 'Name': 'Anchor University, Lagos', 'state': 'Lagos ...', 'Population': '8611', 'age': '22'}\n",
      "{'Rank': '97', 'Name': 'The Technical University', 'state': 'Ibadan', 'Population': '4947', 'age': '45'}\n",
      "{'Rank': '98', 'Name': 'Oduduwa University', 'state': 'Ile Ife', 'Population': '8252', 'age': '11'}\n",
      "{'Rank': '99', 'Name': 'Ondo State University of Science and Technology', 'state': 'Okitipupa', 'Population': '3375', 'age': '18'}\n",
      "{'Rank': '100', 'Name': 'Bauchi State University', 'state': 'Gadau ...', 'Population': '2194', 'age': '20'}\n",
      "{'Rank': '101', 'Name': 'Modibbo Adama University of Technology', 'state': 'Yola', 'Population': '8622', 'age': '30'}\n",
      "{'Rank': '102', 'Name': 'Moshood Abiola University of Science and Technology, Abeokuta', 'state': 'Abeokuta', 'Population': '3600', 'age': '20'}\n",
      "{'Rank': '103', 'Name': 'Kings University', 'state': 'Odeomu', 'Population': '102', 'age': '16'}\n",
      "{'Rank': '104', 'Name': 'Sule Lamido University', 'state': 'Kafin Hausa', 'Population': '8134', 'age': '14'}\n",
      "{'Rank': '105', 'Name': 'Kebbi State University of Science and Technology', 'state': 'Aliero', 'Population': '9730', 'age': '18'}\n",
      "{'Rank': '106', 'Name': 'Ignatius Ajuru University of Education', 'state': 'Port Harcourt', 'Population': '3960', 'age': '17'}\n",
      "{'Rank': '107', 'Name': 'Caritas University', 'state': 'Enugu', 'Population': '1920', 'age': '2022'}\n",
      "{'Rank': '108', 'Name': 'Crescent University, Abeokuta', 'state': 'Abeokuta', 'Population': '1742', 'age': '66'}\n",
      "{'Rank': '109', 'Name': 'Gombe State University', 'state': 'Gombe', 'Population': '3585', 'age': '20'}\n",
      "{'Rank': '110', 'Name': 'Al-Qalam University, Katsina', 'state': 'Katsina', 'Population': '4644', 'age': '17'}\n",
      "{'Rank': '111', 'Name': 'Federal University, Kashere', 'state': 'Kashere', 'Population': '4141', 'age': '17'}\n",
      "{'Rank': '112', 'Name': 'Madonna University, Nigeria', 'state': 'Elele ...', 'Population': '8330', 'age': '17'}\n",
      "{'Rank': '113', 'Name': 'Sokoto State University', 'state': 'Sokoto', 'Population': '5500', 'age': '20'}\n",
      "{'Rank': '114', 'Name': 'Augustine University', 'state': 'Ilara', 'Population': '965', 'age': '1'}\n",
      "{'Rank': '115', 'Name': 'Federal University, Gusau', 'state': 'Gusau', 'Population': '2077', 'age': '30'}\n",
      "{'Rank': '116', 'Name': 'Paul University', 'state': 'Awka', 'Population': '3213', 'age': '1'}\n",
      "{'Rank': '117', 'Name': 'Atiba University', 'state': 'Oyo Town', 'Population': '785', 'age': '26'}\n",
      "{'Rank': '118', 'Name': 'Mcpherson University', 'state': 'Seriki-Sotayo', 'Population': '8237', 'age': '17'}\n",
      "{'Rank': '119', 'Name': 'Plateau State University', 'state': 'Bokkos', 'Population': '1040', 'age': '6'}\n",
      "{'Rank': '120', 'Name': 'Wesley University of Science and Technology', 'state': 'Ondo City', 'Population': '1701', 'age': '10'}\n",
      "{'Rank': '121', 'Name': 'Adamawa State University', 'state': 'Mubi', 'Population': '4755', 'age': '10'}\n",
      "{'Rank': '122', 'Name': 'Rhema University', 'state': 'Aba ...', 'Population': '1770', 'age': '11'}\n",
      "{'Rank': '123', 'Name': 'Novena University', 'state': 'Ogume', 'Population': '6344', 'age': '34'}\n",
      "{'Rank': '124', 'Name': 'Tansian University', 'state': 'Umunya ...', 'Population': '9108', 'age': '41'}\n",
      "{'Rank': '125', 'Name': 'Obong University', 'state': 'Obong Ntak', 'Population': '2722', 'age': '41'}\n",
      "{'Rank': '126', 'Name': 'University of Africa', 'state': 'Toru-Orua ...', 'Population': '6878', 'age': '11'}\n",
      "{'Rank': '127', 'Name': 'Federal University, Wukari', 'state': 'Wukari', 'Population': '3301', 'age': '9'}\n",
      "{'Rank': '128', 'Name': 'Michael and Cecilia Ibru University', 'state': 'Agbara-Otor', 'Population': '746', 'age': '15'}\n",
      "{'Rank': '129', 'Name': 'Gregory University, Uturu', 'state': 'Uturu', 'Population': '9997', 'age': '13'}\n",
      "{'Rank': '130', 'Name': 'PAMO University of Medical Sciences', 'state': 'Port-Harcourt', 'Population': '8874', 'age': '10'}\n",
      "{'Rank': '131', 'Name': 'Nigerian Maritime University, Okerenkoko', 'state': 'Okerenghigho', 'Population': '7224', 'age': '23'}\n",
      "{'Rank': '132', 'Name': 'University of Mkar', 'state': 'Mkar', 'Population': '1927', 'age': '5'}\n",
      "{'Rank': '133', 'Name': 'Admiralty University of Nigeria', 'state': 'Ibusa ...', 'Population': '1895', 'age': '16'}\n",
      "{'Rank': '134', 'Name': 'Dominican University, Ibadan', 'state': 'Ibadan', 'Population': '3069', 'age': '7'}\n",
      "{'Rank': '135', 'Name': 'Wellspring University', 'state': 'Benin City', 'Population': '3424', 'age': '7'}\n",
      "{'Rank': '136', 'Name': 'Christopher University', 'state': 'Mowe', 'Population': '7964', 'age': '39'}\n",
      "{'Rank': '137', 'Name': 'Precious Cornerstone University', 'state': 'Ibadan', 'Population': '3726', 'age': '11'}\n",
      "{'Rank': '138', 'Name': 'Summit University Offa', 'state': 'Offa', 'Population': '4776', 'age': '1'}\n",
      "{'Rank': '139', 'Name': 'Salem University', 'state': 'Lokoja', 'Population': '7214', 'age': '7'}\n",
      "{'Rank': '140', 'Name': 'Glorious Vision University', 'state': 'Ogwa', 'Population': '4170', 'age': '21'}\n",
      "{'Rank': '141', 'Name': 'Renaissance University', 'state': 'Enugu', 'Population': '804', 'age': '39'}\n",
      "{'Rank': '142', 'Name': 'Evangel University, Akaeze', 'state': 'Enugu', 'Population': '9308', 'age': '13'}\n",
      "{'Rank': '143', 'Name': 'Arthur Jarvis University', 'state': 'Calabar', 'Population': '3908', 'age': '30'}\n",
      "{'Rank': '144', 'Name': 'Coal City University', 'state': 'Enugu', 'Population': '5856', 'age': '61'}\n",
      "{'Rank': '145', 'Name': 'Eastern Palm University', 'state': 'Ogboko', 'Population': '8440', 'age': '13'}\n",
      "{'Rank': '146', 'Name': 'Spiritan University, Nneochi', 'state': 'Umunneochi', 'Population': '1978', 'age': '17'}\n",
      "{'Rank': '147', 'Name': 'Ritman University', 'state': 'Ikot Ekpene', 'Population': '8816', 'age': '17'}\n",
      "{'Rank': '148', 'Name': 'Hezekiah University', 'state': 'Umudi', 'Population': '8336', 'age': '4'}\n",
      "{'Rank': '149', 'Name': 'Eko University of Medical and Health Sciences', 'state': 'Ijanikin', 'Population': '1949', 'age': '11'}\n",
      "{'Rank': '150', 'Name': 'Western Delta University', 'state': 'Oghara', 'Population': '8097', 'age': '16'}\n",
      "{'Rank': '151', 'Name': 'Hallmark University, Ijebu-Itele', 'state': 'Ijebu-Itele', 'Population': '7253', 'age': '52'}\n",
      "{'Rank': '152', 'Name': 'Clifford University', 'state': 'Ihie', 'Population': '6922', 'age': '47'}\n",
      "{'Rank': '153', 'Name': 'Crown Hill University', 'state': 'Ilorin', 'Population': '6641', 'age': '1'}\n",
      "{'Rank': '154', 'Name': 'Legacy University, Okija', 'state': 'Okija', 'Population': '2978', 'age': '74'}\n",
      "{'Rank': '155', 'Name': 'Borno State University', 'state': 'Maiduguri', 'Population': '4529', 'age': '51'}\n",
      "{'Rank': '156', 'Name': 'Kwararafa University, Wukari', 'state': 'Wukari', 'Population': '6927', 'age': '60'}\n",
      "{'Rank': '157', 'Name': 'Edwin Clark University', 'state': 'Kiagbodo', 'Population': '7831', 'age': '67'}\n",
      "{'Rank': '158', 'Name': 'Federal University, Gashua', 'state': 'Gashua', 'Population': '1934', 'age': '47'}\n",
      "{'Rank': '159', 'Name': 'Gombe State University of Science and Technology', 'state': 'Kumo', 'Population': '5959', 'age': '15'}\n",
      "{'Rank': '160', 'Name': 'Zamfara State University', 'state': 'Zamfara', 'Population': '6739', 'age': '3'}\n"
     ]
    }
   ],
   "source": [
    "k = school.instantiate_from_csv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "65e4a96a-c1fe-4d29-8fd4-a473150bd0f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: []\n",
       "Index: []"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame(k)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "7f375eb6-f23b-4893-950e-83c275e66edb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[school1 has ('('None',),Lagos ...,13452,42),\n",
       " school1 has ('('None',),Nsukka ...,1075,15),\n",
       " school1 has ('('None',),Ibadan,6515,20),\n",
       " school1 has ('('None',),Ile-Ife,7683,23),\n",
       " school1 has ('('None',),Port Harcourt,3491,12),\n",
       " school1 has ('('None',),Ilorin,9880,13),\n",
       " school1 has ('('None',),Ota,4825,60),\n",
       " school1 has ('('None',),Zaria,3330,17),\n",
       " school1 has ('('None',),Akure,2431,12),\n",
       " school1 has ('('None',),Port Harcourt,6197,17),\n",
       " school1 has ('('None',),Akungba Akoko ...,724,41),\n",
       " school1 has ('('None',),Abeokuta ...,9145,17),\n",
       " school1 has ('('None',),Omu-Aran,6618,22),\n",
       " school1 has ('('None',),Ado-Ekiti,5338,2),\n",
       " school1 has ('('None',),Benin City,9527,63),\n",
       " school1 has ('('None',),Yola,441,22),\n",
       " school1 has ('('None',),Jalingo,1365,45),\n",
       " school1 has ('('None',),Ogbomoso ...,2617,11),\n",
       " school1 has ('('None',),Kano,6545,18),\n",
       " school1 has ('('None',),Jos,2530,20),\n",
       " school1 has ('('None',),Abuja,1983,30),\n",
       " school1 has ('('None',),Ilishan-Remo ...,3345,20),\n",
       " school1 has ('('None',),Abuja,7091,16),\n",
       " school1 has ('('None',),Owerri,725,14),\n",
       " school1 has ('('None',),Lagos,3784,18),\n",
       " school1 has ('('None',),Awka ...,2835,17),\n",
       " school1 has ('('None',),Oye-Ekiti ...,6477,2022),\n",
       " school1 has ('('None',),Abuja,339,66),\n",
       " school1 has ('('None',),Ojo,2083,20),\n",
       " school1 has ('('None',),Abuja,6401,17),\n",
       " school1 has ('('None',),Uyo,16,17),\n",
       " school1 has ('('None',),Minna ...,6684,17),\n",
       " school1 has ('('None',),Sokoto,2191,20),\n",
       " school1 has ('('None',),Lokoja,9353,1),\n",
       " school1 has ('('None',),Abuja,3020,30),\n",
       " school1 has ('('None',),Ago Iwoye ...,5072,1),\n",
       " school1 has ('('None',),Abakaliki,9420,26),\n",
       " school1 has ('('None',),Ado-Ekiti,7005,17),\n",
       " school1 has ('('None',),Ede ...,803,6),\n",
       " school1 has ('('None',),Otuoke,816,10),\n",
       " school1 has ('('None',),Makurdi,9083,10),\n",
       " school1 has ('('None',),Keffi,4670,11),\n",
       " school1 has ('('None',),Calabar,8675,34),\n",
       " school1 has ('('None',),Ijebu-Ode ...,9229,41),\n",
       " school1 has ('('None',),Maiduguri,6493,41),\n",
       " school1 has ('('None',),Oshogbo ...,7659,11),\n",
       " school1 has ('('None',),Ilorin,1950,9),\n",
       " school1 has ('('None',),Iwo,5623,15),\n",
       " school1 has ('('None',),Bauchi,6962,13),\n",
       " school1 has ('('None',),Katsina,1285,10),\n",
       " school1 has ('('None',),Kano,5941,23),\n",
       " school1 has ('('None',),Dutsin-Ma,5310,5),\n",
       " school1 has ('('None',),Kaduna,5802,16),\n",
       " school1 has ('('None',),Uturu,861,7),\n",
       " school1 has ('('None',),Abraka,5959,7),\n",
       " school1 has ('('None',),Enugu,3603,39),\n",
       " school1 has ('('None',),Makogi Oba,8327,11),\n",
       " school1 has ('('None',),Lafia,1699,1),\n",
       " school1 has ('('None',),Umuahia,7318,7),\n",
       " school1 has ('('None',),Ikwo,5814,21),\n",
       " school1 has ('('None',),Ibadan,9848,39),\n",
       " school1 has ('('None',),Calabar ...,9112,13),\n",
       " school1 has ('('None',),Uli ...,5330,30),\n",
       " school1 has ('('None',),Ikot Akpad ...,7257,61),\n",
       " school1 has ('('None',),Makurdi,5678,13),\n",
       " school1 has ('('None',),Ugwuomu-Nike ...,8412,17),\n",
       " school1 has ('('None',),Dutse,5307,17),\n",
       " school1 has ('('None',),Iyamho,3243,4),\n",
       " school1 has ('('None',),Ilorin ...,1130,11),\n",
       " school1 has ('('None',),Kano,4912,16),\n",
       " school1 has ('('None',),Ekpoma,2562,52),\n",
       " school1 has ('('None',),Okada ...,9084,47),\n",
       " school1 has ('('None',),Effurun,1516,1),\n",
       " school1 has ('('None',),Faith City ...,3924,74),\n",
       " school1 has ('('None',),Ondo City,2407,51),\n",
       " school1 has ('('None',),Owerri,95,60),\n",
       " school1 has ('('None',),Wilberforce Island,2148,67),\n",
       " school1 has ('('None',),Ota,761,47),\n",
       " school1 has ('('None',),Benin City,155,15),\n",
       " school1 has ('('None',),Anyigba,1586,3),\n",
       " school1 has ('('None',),Ede,8340,42),\n",
       " school1 has ('('None',),Oyo Town,735,15),\n",
       " school1 has ('('None',),Lapai,1118,20),\n",
       " school1 has ('('None',),Ilara-Mokin,8871,23),\n",
       " school1 has ('('None',),Okun Owa,5403,12),\n",
       " school1 has ('('None',),Abeokuta,9158,13),\n",
       " school1 has ('('None',),Imota,609,60),\n",
       " school1 has ('('None',),Ikeji-Arakeji,7261,17),\n",
       " school1 has ('('None',),Auta Balifi,8650,12),\n",
       " school1 has ('('None',),Oshogbo,1344,17),\n",
       " school1 has ('('None',),Ibadan,3941,41),\n",
       " school1 has ('('None',),Owo,2070,17),\n",
       " school1 has ('('None',),Damaturu,3394,22),\n",
       " school1 has ('('None',),Wudil,2605,2),\n",
       " school1 has ('('None',),Birnin Kebbi,6425,63),\n",
       " school1 has ('('None',),Lagos ...,8611,22),\n",
       " school1 has ('('None',),Ibadan,4947,45),\n",
       " school1 has ('('None',),Ile Ife,8252,11),\n",
       " school1 has ('('None',),Okitipupa,3375,18),\n",
       " school1 has ('('None',),Gadau ...,2194,20),\n",
       " school1 has ('('None',),Yola,8622,30),\n",
       " school1 has ('('None',),Abeokuta,3600,20),\n",
       " school1 has ('('None',),Odeomu,102,16),\n",
       " school1 has ('('None',),Kafin Hausa,8134,14),\n",
       " school1 has ('('None',),Aliero,9730,18),\n",
       " school1 has ('('None',),Port Harcourt,3960,17),\n",
       " school1 has ('('None',),Enugu,1920,2022),\n",
       " school1 has ('('None',),Abeokuta,1742,66),\n",
       " school1 has ('('None',),Gombe,3585,20),\n",
       " school1 has ('('None',),Katsina,4644,17),\n",
       " school1 has ('('None',),Kashere,4141,17),\n",
       " school1 has ('('None',),Elele ...,8330,17),\n",
       " school1 has ('('None',),Sokoto,5500,20),\n",
       " school1 has ('('None',),Ilara,965,1),\n",
       " school1 has ('('None',),Gusau,2077,30),\n",
       " school1 has ('('None',),Awka,3213,1),\n",
       " school1 has ('('None',),Oyo Town,785,26),\n",
       " school1 has ('('None',),Seriki-Sotayo,8237,17),\n",
       " school1 has ('('None',),Bokkos,1040,6),\n",
       " school1 has ('('None',),Ondo City,1701,10),\n",
       " school1 has ('('None',),Mubi,4755,10),\n",
       " school1 has ('('None',),Aba ...,1770,11),\n",
       " school1 has ('('None',),Ogume,6344,34),\n",
       " school1 has ('('None',),Umunya ...,9108,41),\n",
       " school1 has ('('None',),Obong Ntak,2722,41),\n",
       " school1 has ('('None',),Toru-Orua ...,6878,11),\n",
       " school1 has ('('None',),Wukari,3301,9),\n",
       " school1 has ('('None',),Agbara-Otor,746,15),\n",
       " school1 has ('('None',),Uturu,9997,13),\n",
       " school1 has ('('None',),Port-Harcourt,8874,10),\n",
       " school1 has ('('None',),Okerenghigho,7224,23),\n",
       " school1 has ('('None',),Mkar,1927,5),\n",
       " school1 has ('('None',),Ibusa ...,1895,16),\n",
       " school1 has ('('None',),Ibadan,3069,7),\n",
       " school1 has ('('None',),Benin City,3424,7),\n",
       " school1 has ('('None',),Mowe,7964,39),\n",
       " school1 has ('('None',),Ibadan,3726,11),\n",
       " school1 has ('('None',),Offa,4776,1),\n",
       " school1 has ('('None',),Lokoja,7214,7),\n",
       " school1 has ('('None',),Ogwa,4170,21),\n",
       " school1 has ('('None',),Enugu,804,39),\n",
       " school1 has ('('None',),Enugu,9308,13),\n",
       " school1 has ('('None',),Calabar,3908,30),\n",
       " school1 has ('('None',),Enugu,5856,61),\n",
       " school1 has ('('None',),Ogboko,8440,13),\n",
       " school1 has ('('None',),Umunneochi,1978,17),\n",
       " school1 has ('('None',),Ikot Ekpene,8816,17),\n",
       " school1 has ('('None',),Umudi,8336,4),\n",
       " school1 has ('('None',),Ijanikin,1949,11),\n",
       " school1 has ('('None',),Oghara,8097,16),\n",
       " school1 has ('('None',),Ijebu-Itele,7253,52),\n",
       " school1 has ('('None',),Ihie,6922,47),\n",
       " school1 has ('('None',),Ilorin,6641,1),\n",
       " school1 has ('('None',),Okija,2978,74),\n",
       " school1 has ('('None',),Maiduguri,4529,51),\n",
       " school1 has ('('None',),Wukari,6927,60),\n",
       " school1 has ('('None',),Kiagbodo,7831,67),\n",
       " school1 has ('('None',),Gashua,1934,47),\n",
       " school1 has ('('None',),Kumo,5959,15),\n",
       " school1 has ('('None',),Zamfara,6739,3)]"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "school.all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "c77465a0-fc67-4f08-9431-2b2f5293ccf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<built-in method is_integer of float object at 0x000001DEAC981250>\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "school.is_integer(40.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63c13717-35a4-4ad9-b970-85958c0ef5b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "40.0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "f00d0b6c-9635-4b31-a43e-296a11c4456c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mappingproxy({'__module__': '__main__',\n",
       "              'schoolfees': 0.3142,\n",
       "              'all': [school1 has ('('None',),Osun state,747,2),\n",
       "               school1 has ('('None',),Delat state,123,8),\n",
       "               school1 has ('('None',),Edo state,861,12),\n",
       "               school1 has ('('None',),Ondo state,133,21),\n",
       "               school1 has ('('None',),Rivers state,222,4)],\n",
       "              '__init__': <function __main__.school.__init__(self, name: str, location: str, population: int, age: int, eff=0)>,\n",
       "              'rating': <function __main__.school.rating(self, a, b)>,\n",
       "              'rating1': <function __main__.school.rating1(self)>,\n",
       "              'schfees': <function __main__.school.schfees(self)>,\n",
       "              '__repr__': <function __main__.school.__repr__(self)>,\n",
       "              'instantiate_from_csv': <classmethod at 0x1deada044f0>,\n",
       "              '__dict__': <attribute '__dict__' of 'school' objects>,\n",
       "              '__weakref__': <attribute '__weakref__' of 'school' objects>,\n",
       "              '__doc__': None})"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "school.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "24362437-3749-4b69-ab94-1244045f17da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "40.5.isinstance(40, int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "6816c5bb-6ced-4b39-a8f4-14d6424bb661",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "type object 'school' has no attribute 'location'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[1;32mIn [126]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mschool\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mlocation\u001b[49m\n",
      "\u001b[1;31mAttributeError\u001b[0m: type object 'school' has no attribute 'location'"
     ]
    }
   ],
   "source": [
    "school.location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "b5ad7cdc-7a4d-4425-b0dc-47f070ac6325",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "347\n",
      "609\n",
      "458\n",
      "350\n",
      "233\n"
     ]
    }
   ],
   "source": [
    "for i in school1.all:\n",
    "    print(i.population )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "562ca4dc-e439-47d8-9560-51f74812849a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "school1 has ('('Fav',),Osun state,347,2)"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "school1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc7e5dfe-0ce0-4425-88cd-e1260d775a35",
   "metadata": {},
   "source": [
    "# Version 2.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "c724b3b9-7526-42cd-94cc-50328b4e2564",
   "metadata": {},
   "outputs": [],
   "source": [
    "# University orentation software"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7bf1949-6729-4d9e-9913-b3b76483071f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "cfefb03a-0bb2-46ec-89fd-763615719e5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "class university:\n",
    "  \n",
    "    \n",
    "    univerityfees = 0.3142 #schoolfees is a class level variable \n",
    "    \n",
    "# the __init__ function is an inbuilt special function that initialzes when a class instance is created\n",
    "#-- certain attributes can be optional on a instance by intializing it to zero\n",
    "# each value datatype can be included \n",
    "\n",
    "    all =[] # a list for alll instances created in a class\n",
    "    def __init__ (self,  rank: int, name: str, location: str, population: int, age: int):\n",
    "        assert age >= 0, f'The age {age} cannot be less than 0'                      # The age cannot be less than 0\n",
    "        assert population >= 0, f'The population {population} cannot be less than 0'  # The population cannot be less than 0\n",
    "        assert rank >=0, f'The rank {population} cannot be less than 0'\n",
    "    # Assign to self objects instance attributes\n",
    "        self.rank = rank\n",
    "        self.name = name\n",
    "        self.location = location\n",
    "        self.population = population\n",
    "        self.age = age \n",
    "    def schfees(self):\n",
    "        return (Univerity.schoolfees) * (self.population)\n",
    "   \n",
    "    # each instance of school is an Object to rename that object we use the special method __repr__\n",
    "    def __repr__(self):\n",
    "        return f\"Univerity has ('{self.name,},{self.location},{self.population},{self.age})\"\n",
    "    \n",
    "    # Each method from a csv file is instatiated to create an object with the required properties\n",
    "    \n",
    "    # Creating a class method  i.e this method can only be accessed by the class itself not its instances\n",
    "    @classmethod\n",
    "    def instantiate_from_csv(cls):#cls means class, te class method can call itself and also use self but this wil be confusing \n",
    "        with open(\"C:/Users/hp/Downloads/Documents/Book1.csv\", 'r') as f:  #'F' is the variable holding the csv \n",
    "            reader = csv.DictReader(f)\n",
    "            schools = list(reader)\n",
    "            print(f)\n",
    "        for i in schools:\n",
    "            print(i)\n",
    "        for i in schools:\n",
    "            university(\n",
    "               rank = int(i.get('rank')),\n",
    "               name = str(i.get('name')),\n",
    "               location = str(i.get('state')),\n",
    "               population = int(i.get('Population')),\n",
    "                age = int(i.get('age'))\n",
    "                )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "d7053100-18fb-425a-b236-1d0a2670cb23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='C:/Users/hp/Downloads/Documents/Book1.csv' mode='r' encoding='cp1252'>\n",
      "{'rank': '1', 'Name': 'University of Lagos', 'state': 'Lagos ...', 'Population': '13452', 'age': '42'}\n",
      "{'rank': '2', 'Name': 'University of Nigeria', 'state': 'Nsukka ...', 'Population': '1075', 'age': '15'}\n",
      "{'rank': '3', 'Name': 'University of Ibadan', 'state': 'Ibadan', 'Population': '6515', 'age': '20'}\n",
      "{'rank': '4', 'Name': 'Obafemi Awolowo University', 'state': 'Ile-Ife', 'Population': '7683', 'age': '23'}\n",
      "{'rank': '5', 'Name': 'University of Port Harcourt', 'state': 'Port Harcourt', 'Population': '3491', 'age': '12'}\n",
      "{'rank': '6', 'Name': 'University of Ilorin', 'state': 'Ilorin', 'Population': '9880', 'age': '13'}\n",
      "{'rank': '7', 'Name': 'Covenant University', 'state': 'Ota', 'Population': '4825', 'age': '60'}\n",
      "{'rank': '8', 'Name': 'Ahmadu Bello University', 'state': 'Zaria', 'Population': '3330', 'age': '17'}\n",
      "{'rank': '9', 'Name': 'Federal University of Technology, Akure', 'state': 'Akure', 'Population': '2431', 'age': '12'}\n",
      "{'rank': '10', 'Name': 'Rivers State University', 'state': 'Port Harcourt', 'Population': '6197', 'age': '17'}\n",
      "{'rank': '11', 'Name': 'Adekunle Ajasin University', 'state': 'Akungba Akoko ...', 'Population': '724', 'age': '41'}\n",
      "{'rank': '12', 'Name': 'Federal University of Agriculture, Abeokuta', 'state': 'Abeokuta ...', 'Population': '9145', 'age': '17'}\n",
      "{'rank': '13', 'Name': 'Landmark University', 'state': 'Omu-Aran', 'Population': '6618', 'age': '22'}\n",
      "{'rank': '14', 'Name': 'Afe Babalola University', 'state': 'Ado-Ekiti', 'Population': '5338', 'age': '2'}\n",
      "{'rank': '15', 'Name': 'University of Benin', 'state': 'Benin City', 'Population': '9527', 'age': '63'}\n",
      "{'rank': '16', 'Name': 'American University of Nigeria', 'state': 'Yola', 'Population': '441', 'age': '22'}\n",
      "{'rank': '17', 'Name': 'Taraba State University', 'state': 'Jalingo', 'Population': '1365', 'age': '45'}\n",
      "{'rank': '18', 'Name': 'Ladoke Akintola University of Technology', 'state': 'Ogbomoso ...', 'Population': '2617', 'age': '11'}\n",
      "{'rank': '19', 'Name': 'Bayero University Kano', 'state': 'Kano', 'Population': '6545', 'age': '18'}\n",
      "{'rank': '20', 'Name': 'University of Jos', 'state': 'Jos', 'Population': '2530', 'age': '20'}\n",
      "{'rank': '21', 'Name': 'University of Abuja', 'state': 'Abuja', 'Population': '1983', 'age': '30'}\n",
      "{'rank': '22', 'Name': 'Babcock University', 'state': 'Ilishan-Remo ...', 'Population': '3345', 'age': '20'}\n",
      "{'rank': '23', 'Name': 'Nile University of Nigeria', 'state': 'Abuja', 'Population': '7091', 'age': '16'}\n",
      "{'rank': '24', 'Name': 'Federal University of Technology, Owerri', 'state': 'Owerri', 'Population': '725', 'age': '14'}\n",
      "{'rank': '25', 'Name': 'Pan-Atlantic University', 'state': 'Lagos', 'Population': '3784', 'age': '18'}\n",
      "{'rank': '26', 'Name': 'Nnamdi Azikiwe University', 'state': 'Awka ...', 'Population': '2835', 'age': '17'}\n",
      "{'rank': '27', 'Name': 'Federal University, Oye-Ekiti', 'state': 'Oye-Ekiti ...', 'Population': '6477', 'age': '2022'}\n",
      "{'rank': '28', 'Name': 'Veritas University', 'state': 'Abuja', 'Population': '339', 'age': '66'}\n",
      "{'rank': '29', 'Name': 'Lagos State University', 'state': 'Ojo', 'Population': '2083', 'age': '20'}\n",
      "{'rank': '30', 'Name': 'Baze University', 'state': 'Abuja', 'Population': '6401', 'age': '17'}\n",
      "{'rank': '31', 'Name': 'University of Uyo', 'state': 'Uyo', 'Population': '16', 'age': '17'}\n",
      "{'rank': '32', 'Name': 'Federal University of Technology, Minna', 'state': 'Minna ...', 'Population': '6684', 'age': '17'}\n",
      "{'rank': '33', 'Name': 'Usmanu Danfodio University', 'state': 'Sokoto', 'Population': '2191', 'age': '20'}\n",
      "{'rank': '34', 'Name': 'Federal University, Lokoja', 'state': 'Lokoja', 'Population': '9353', 'age': '1'}\n",
      "{'rank': '35', 'Name': 'African University of Science and Technology', 'state': 'Abuja', 'Population': '3020', 'age': '30'}\n",
      "{'rank': '36', 'Name': 'Olabisi Onabanjo University', 'state': 'Ago Iwoye ...', 'Population': '5072', 'age': '1'}\n",
      "{'rank': '37', 'Name': 'Ebonyi State University', 'state': 'Abakaliki', 'Population': '9420', 'age': '26'}\n",
      "{'rank': '38', 'Name': 'Ekiti State University, Ado Ekiti', 'state': 'Ado-Ekiti', 'Population': '7005', 'age': '17'}\n",
      "{'rank': '39', 'Name': \"Redeemer's University\", 'state': 'Ede ...', 'Population': '803', 'age': '6'}\n",
      "{'rank': '40', 'Name': 'Federal University, Otuoke', 'state': 'Otuoke', 'Population': '816', 'age': '10'}\n",
      "{'rank': '41', 'Name': 'Benue State University', 'state': 'Makurdi', 'Population': '9083', 'age': '10'}\n",
      "{'rank': '42', 'Name': 'Nasarawa State University', 'state': 'Keffi', 'Population': '4670', 'age': '11'}\n",
      "{'rank': '43', 'Name': 'University of Calabar', 'state': 'Calabar', 'Population': '8675', 'age': '34'}\n",
      "{'rank': '44', 'Name': 'Tai Solarin University of Education', 'state': 'Ijebu-Ode ...', 'Population': '9229', 'age': '41'}\n",
      "{'rank': '45', 'Name': 'University of Maiduguri', 'state': 'Maiduguri', 'Population': '6493', 'age': '41'}\n",
      "{'rank': '46', 'Name': 'Osun State University', 'state': 'Oshogbo ...', 'Population': '7659', 'age': '11'}\n",
      "{'rank': '47', 'Name': 'Kwara State University', 'state': 'Ilorin', 'Population': '1950', 'age': '9'}\n",
      "{'rank': '48', 'Name': 'Bowen University', 'state': 'Iwo', 'Population': '5623', 'age': '15'}\n",
      "{'rank': '49', 'Name': 'Abubakar Tafawa Balewa University', 'state': 'Bauchi', 'Population': '6962', 'age': '13'}\n",
      "{'rank': '50', 'Name': \"Umaru Musa Yar'Adua University\", 'state': 'Katsina', 'Population': '1285', 'age': '10'}\n",
      "{'rank': '51', 'Name': 'Skyline University Nigeria', 'state': 'Kano', 'Population': '5941', 'age': '23'}\n",
      "{'rank': '52', 'Name': 'Federal University, Dutsin-Ma', 'state': 'Dutsin-Ma', 'Population': '5310', 'age': '5'}\n",
      "{'rank': '53', 'Name': 'Kaduna State University', 'state': 'Kaduna', 'Population': '5802', 'age': '16'}\n",
      "{'rank': '54', 'Name': 'Abia State University', 'state': 'Uturu', 'Population': '861', 'age': '7'}\n",
      "{'rank': '55', 'Name': 'Delta State University, Abraka', 'state': 'Abraka', 'Population': '5959', 'age': '7'}\n",
      "{'rank': '56', 'Name': 'Enugu State University of Science and Technology', 'state': 'Enugu', 'Population': '3603', 'age': '39'}\n",
      "{'rank': '57', 'Name': 'Mountain Top University', 'state': 'Makogi Oba', 'Population': '8327', 'age': '11'}\n",
      "{'rank': '58', 'Name': 'Federal University, Lafia', 'state': 'Lafia', 'Population': '1699', 'age': '1'}\n",
      "{'rank': '59', 'Name': 'Michael Okpara University of Agriculture', 'state': 'Umuahia', 'Population': '7318', 'age': '7'}\n",
      "{'rank': '60', 'Name': 'Alex Ekwueme Federal University, Ndufu-Alike', 'state': 'Ikwo', 'Population': '5814', 'age': '21'}\n",
      "{'rank': '61', 'Name': 'Lead City University', 'state': 'Ibadan', 'Population': '9848', 'age': '39'}\n",
      "{'rank': '62', 'Name': 'Cross River University of Technology', 'state': 'Calabar ...', 'Population': '9112', 'age': '13'}\n",
      "{'rank': '63', 'Name': 'Chukwuemeka Odumegwu Ojukwu University', 'state': 'Uli ...', 'Population': '5330', 'age': '30'}\n",
      "{'rank': '64', 'Name': 'Akwa Ibom State University', 'state': 'Ikot Akpad ...', 'Population': '7257', 'age': '61'}\n",
      "{'rank': '65', 'Name': 'University of Agriculture, Makurdi', 'state': 'Makurdi', 'Population': '5678', 'age': '13'}\n",
      "{'rank': '66', 'Name': 'Godfrey Okoye University', 'state': 'Ugwuomu-Nike ...', 'Population': '8412', 'age': '17'}\n",
      "{'rank': '67', 'Name': 'Federal University, Dutse', 'state': 'Dutse', 'Population': '5307', 'age': '17'}\n",
      "{'rank': '68', 'Name': 'Edo University', 'state': 'Iyamho', 'Population': '3243', 'age': '4'}\n",
      "{'rank': '69', 'Name': 'Al-Hikmah University', 'state': 'Ilorin ...', 'Population': '1130', 'age': '11'}\n",
      "{'rank': '70', 'Name': 'Yusuf Maitama Sule University Kano', 'state': 'Kano', 'Population': '4912', 'age': '16'}\n",
      "{'rank': '71', 'Name': 'Ambrose Alli University', 'state': 'Ekpoma', 'Population': '2562', 'age': '52'}\n",
      "{'rank': '72', 'Name': 'Igbinedion University Okada', 'state': 'Okada ...', 'Population': '9084', 'age': '47'}\n",
      "{'rank': '73', 'Name': 'Federal University of Petroleum Resources', 'state': 'Effurun', 'Population': '1516', 'age': '1'}\n",
      "{'rank': '74', 'Name': 'Crawford University', 'state': 'Faith City ...', 'Population': '3924', 'age': '74'}\n",
      "{'rank': '75', 'Name': 'University of Medical Sciences', 'state': 'Ondo City', 'Population': '2407', 'age': '51'}\n",
      "{'rank': '76', 'Name': 'Imo State University', 'state': 'Owerri', 'Population': '95', 'age': '60'}\n",
      "{'rank': '77', 'Name': 'Niger Delta University', 'state': 'Wilberforce Island', 'Population': '2148', 'age': '67'}\n",
      "{'rank': '78', 'Name': 'Bells University of Technology', 'state': 'Ota', 'Population': '761', 'age': '47'}\n",
      "{'rank': '79', 'Name': 'Benson Idahosa University', 'state': 'Benin City', 'Population': '155', 'age': '15'}\n",
      "{'rank': '80', 'Name': 'Kogi State University', 'state': 'Anyigba', 'Population': '1586', 'age': '3'}\n",
      "{'rank': '81', 'Name': 'Adeleke University', 'state': 'Ede', 'Population': '8340', 'age': '42'}\n",
      "{'rank': '82', 'Name': 'Ajayi Crowther University', 'state': 'Oyo Town', 'Population': '735', 'age': '15'}\n",
      "{'rank': '83', 'Name': 'Ibrahim Badamasi Babangida University', 'state': 'Lapai', 'Population': '1118', 'age': '20'}\n",
      "{'rank': '84', 'Name': 'Elizade University', 'state': 'Ilara-Mokin', 'Population': '8871', 'age': '23'}\n",
      "{'rank': '85', 'Name': 'Southwestern University, Nigeria', 'state': 'Okun Owa', 'Population': '5403', 'age': '12'}\n",
      "{'rank': '86', 'Name': 'Chrisland University', 'state': 'Abeokuta', 'Population': '9158', 'age': '13'}\n",
      "{'rank': '87', 'Name': 'Caleb University', 'state': 'Imota', 'Population': '609', 'age': '60'}\n",
      "{'rank': '88', 'Name': 'Joseph Ayo Babalola University', 'state': 'Ikeji-Arakeji', 'Population': '7261', 'age': '17'}\n",
      "{'rank': '89', 'Name': 'Bingham University', 'state': 'Auta Balifi', 'Population': '8650', 'age': '12'}\n",
      "{'rank': '90', 'Name': 'Fountain University, Osogbo', 'state': 'Oshogbo', 'Population': '1344', 'age': '17'}\n",
      "{'rank': '91', 'Name': 'Kola Daisi University', 'state': 'Ibadan', 'Population': '3941', 'age': '41'}\n",
      "{'rank': '92', 'Name': 'Achievers University, Owo', 'state': 'Owo', 'Population': '2070', 'age': '17'}\n",
      "{'rank': '93', 'Name': 'Yobe State University', 'state': 'Damaturu', 'Population': '3394', 'age': '22'}\n",
      "{'rank': '94', 'Name': 'Kano University of Science and Technology', 'state': 'Wudil', 'Population': '2605', 'age': '2'}\n",
      "{'rank': '95', 'Name': 'Federal University, Birnin Kebbi', 'state': 'Birnin Kebbi', 'Population': '6425', 'age': '63'}\n",
      "{'rank': '96', 'Name': 'Anchor University, Lagos', 'state': 'Lagos ...', 'Population': '8611', 'age': '22'}\n",
      "{'rank': '97', 'Name': 'The Technical University', 'state': 'Ibadan', 'Population': '4947', 'age': '45'}\n",
      "{'rank': '98', 'Name': 'Oduduwa University', 'state': 'Ile Ife', 'Population': '8252', 'age': '11'}\n",
      "{'rank': '99', 'Name': 'Ondo State University of Science and Technology', 'state': 'Okitipupa', 'Population': '3375', 'age': '18'}\n",
      "{'rank': '100', 'Name': 'Bauchi State University', 'state': 'Gadau ...', 'Population': '2194', 'age': '20'}\n",
      "{'rank': '101', 'Name': 'Modibbo Adama University of Technology', 'state': 'Yola', 'Population': '8622', 'age': '30'}\n",
      "{'rank': '102', 'Name': 'Moshood Abiola University of Science and Technology, Abeokuta', 'state': 'Abeokuta', 'Population': '3600', 'age': '20'}\n",
      "{'rank': '103', 'Name': 'Kings University', 'state': 'Odeomu', 'Population': '102', 'age': '16'}\n",
      "{'rank': '104', 'Name': 'Sule Lamido University', 'state': 'Kafin Hausa', 'Population': '8134', 'age': '14'}\n",
      "{'rank': '105', 'Name': 'Kebbi State University of Science and Technology', 'state': 'Aliero', 'Population': '9730', 'age': '18'}\n",
      "{'rank': '106', 'Name': 'Ignatius Ajuru University of Education', 'state': 'Port Harcourt', 'Population': '3960', 'age': '17'}\n",
      "{'rank': '107', 'Name': 'Caritas University', 'state': 'Enugu', 'Population': '1920', 'age': '2022'}\n",
      "{'rank': '108', 'Name': 'Crescent University, Abeokuta', 'state': 'Abeokuta', 'Population': '1742', 'age': '66'}\n",
      "{'rank': '109', 'Name': 'Gombe State University', 'state': 'Gombe', 'Population': '3585', 'age': '20'}\n",
      "{'rank': '110', 'Name': 'Al-Qalam University, Katsina', 'state': 'Katsina', 'Population': '4644', 'age': '17'}\n",
      "{'rank': '111', 'Name': 'Federal University, Kashere', 'state': 'Kashere', 'Population': '4141', 'age': '17'}\n",
      "{'rank': '112', 'Name': 'Madonna University, Nigeria', 'state': 'Elele ...', 'Population': '8330', 'age': '17'}\n",
      "{'rank': '113', 'Name': 'Sokoto State University', 'state': 'Sokoto', 'Population': '5500', 'age': '20'}\n",
      "{'rank': '114', 'Name': 'Augustine University', 'state': 'Ilara', 'Population': '965', 'age': '1'}\n",
      "{'rank': '115', 'Name': 'Federal University, Gusau', 'state': 'Gusau', 'Population': '2077', 'age': '30'}\n",
      "{'rank': '116', 'Name': 'Paul University', 'state': 'Awka', 'Population': '3213', 'age': '1'}\n",
      "{'rank': '117', 'Name': 'Atiba University', 'state': 'Oyo Town', 'Population': '785', 'age': '26'}\n",
      "{'rank': '118', 'Name': 'Mcpherson University', 'state': 'Seriki-Sotayo', 'Population': '8237', 'age': '17'}\n",
      "{'rank': '119', 'Name': 'Plateau State University', 'state': 'Bokkos', 'Population': '1040', 'age': '6'}\n",
      "{'rank': '120', 'Name': 'Wesley University of Science and Technology', 'state': 'Ondo City', 'Population': '1701', 'age': '10'}\n",
      "{'rank': '121', 'Name': 'Adamawa State University', 'state': 'Mubi', 'Population': '4755', 'age': '10'}\n",
      "{'rank': '122', 'Name': 'Rhema University', 'state': 'Aba ...', 'Population': '1770', 'age': '11'}\n",
      "{'rank': '123', 'Name': 'Novena University', 'state': 'Ogume', 'Population': '6344', 'age': '34'}\n",
      "{'rank': '124', 'Name': 'Tansian University', 'state': 'Umunya ...', 'Population': '9108', 'age': '41'}\n",
      "{'rank': '125', 'Name': 'Obong University', 'state': 'Obong Ntak', 'Population': '2722', 'age': '41'}\n",
      "{'rank': '126', 'Name': 'University of Africa', 'state': 'Toru-Orua ...', 'Population': '6878', 'age': '11'}\n",
      "{'rank': '127', 'Name': 'Federal University, Wukari', 'state': 'Wukari', 'Population': '3301', 'age': '9'}\n",
      "{'rank': '128', 'Name': 'Michael and Cecilia Ibru University', 'state': 'Agbara-Otor', 'Population': '746', 'age': '15'}\n",
      "{'rank': '129', 'Name': 'Gregory University, Uturu', 'state': 'Uturu', 'Population': '9997', 'age': '13'}\n",
      "{'rank': '130', 'Name': 'PAMO University of Medical Sciences', 'state': 'Port-Harcourt', 'Population': '8874', 'age': '10'}\n",
      "{'rank': '131', 'Name': 'Nigerian Maritime University, Okerenkoko', 'state': 'Okerenghigho', 'Population': '7224', 'age': '23'}\n",
      "{'rank': '132', 'Name': 'University of Mkar', 'state': 'Mkar', 'Population': '1927', 'age': '5'}\n",
      "{'rank': '133', 'Name': 'Admiralty University of Nigeria', 'state': 'Ibusa ...', 'Population': '1895', 'age': '16'}\n",
      "{'rank': '134', 'Name': 'Dominican University, Ibadan', 'state': 'Ibadan', 'Population': '3069', 'age': '7'}\n",
      "{'rank': '135', 'Name': 'Wellspring University', 'state': 'Benin City', 'Population': '3424', 'age': '7'}\n",
      "{'rank': '136', 'Name': 'Christopher University', 'state': 'Mowe', 'Population': '7964', 'age': '39'}\n",
      "{'rank': '137', 'Name': 'Precious Cornerstone University', 'state': 'Ibadan', 'Population': '3726', 'age': '11'}\n",
      "{'rank': '138', 'Name': 'Summit University Offa', 'state': 'Offa', 'Population': '4776', 'age': '1'}\n",
      "{'rank': '139', 'Name': 'Salem University', 'state': 'Lokoja', 'Population': '7214', 'age': '7'}\n",
      "{'rank': '140', 'Name': 'Glorious Vision University', 'state': 'Ogwa', 'Population': '4170', 'age': '21'}\n",
      "{'rank': '141', 'Name': 'Renaissance University', 'state': 'Enugu', 'Population': '804', 'age': '39'}\n",
      "{'rank': '142', 'Name': 'Evangel University, Akaeze', 'state': 'Enugu', 'Population': '9308', 'age': '13'}\n",
      "{'rank': '143', 'Name': 'Arthur Jarvis University', 'state': 'Calabar', 'Population': '3908', 'age': '30'}\n",
      "{'rank': '144', 'Name': 'Coal City University', 'state': 'Enugu', 'Population': '5856', 'age': '61'}\n",
      "{'rank': '145', 'Name': 'Eastern Palm University', 'state': 'Ogboko', 'Population': '8440', 'age': '13'}\n",
      "{'rank': '146', 'Name': 'Spiritan University, Nneochi', 'state': 'Umunneochi', 'Population': '1978', 'age': '17'}\n",
      "{'rank': '147', 'Name': 'Ritman University', 'state': 'Ikot Ekpene', 'Population': '8816', 'age': '17'}\n",
      "{'rank': '148', 'Name': 'Hezekiah University', 'state': 'Umudi', 'Population': '8336', 'age': '4'}\n",
      "{'rank': '149', 'Name': 'Eko University of Medical and Health Sciences', 'state': 'Ijanikin', 'Population': '1949', 'age': '11'}\n",
      "{'rank': '150', 'Name': 'Western Delta University', 'state': 'Oghara', 'Population': '8097', 'age': '16'}\n",
      "{'rank': '151', 'Name': 'Hallmark University, Ijebu-Itele', 'state': 'Ijebu-Itele', 'Population': '7253', 'age': '52'}\n",
      "{'rank': '152', 'Name': 'Clifford University', 'state': 'Ihie', 'Population': '6922', 'age': '47'}\n",
      "{'rank': '153', 'Name': 'Crown Hill University', 'state': 'Ilorin', 'Population': '6641', 'age': '1'}\n",
      "{'rank': '154', 'Name': 'Legacy University, Okija', 'state': 'Okija', 'Population': '2978', 'age': '74'}\n",
      "{'rank': '155', 'Name': 'Borno State University', 'state': 'Maiduguri', 'Population': '4529', 'age': '51'}\n",
      "{'rank': '156', 'Name': 'Kwararafa University, Wukari', 'state': 'Wukari', 'Population': '6927', 'age': '60'}\n",
      "{'rank': '157', 'Name': 'Edwin Clark University', 'state': 'Kiagbodo', 'Population': '7831', 'age': '67'}\n",
      "{'rank': '158', 'Name': 'Federal University, Gashua', 'state': 'Gashua', 'Population': '1934', 'age': '47'}\n",
      "{'rank': '159', 'Name': 'Gombe State University of Science and Technology', 'state': 'Kumo', 'Population': '5959', 'age': '15'}\n",
      "{'rank': '160', 'Name': 'Zamfara State University', 'state': 'Zamfara', 'Population': '6739', 'age': '3'}\n"
     ]
    }
   ],
   "source": [
    "university.instantiate_from_csv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fd74f166-c31e-41b5-b4d2-34d4906d9dff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "4d891995-ac77-4ebe-b3cf-ab3e1f713876",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Faculties(university):\n",
    "    # faculties is a cild class of university carrying all its properties through a process call inheritance\n",
    "    all = []\n",
    "    def __init__ (self,  rank: int, name: str, location: str, population: int, age: int, faculty: str):\n",
    "        super().__init__(rank, name, location, population, age)\n",
    "            # Assign to self objects instance attributes\n",
    "        self.faculty  = faculty\n",
    "        #self.rank = rank\n",
    "        Faculties.all.append(self)\n",
    "    def __repr__(self):\n",
    "        return f\" {self.__class__.__name__},{self.rank},{self.name,},{self.location},{self.population},{self.age},{self.faculty})\"\n",
    "    \n",
    "fac = Faculties(9,'Federal University of Technology','Ondo', 2431 , 12, 'Engineering')\n",
    "fac.age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "71e71845-424c-4073-a1b9-8ddc45ae96f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "university.all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "4735af0e-fd7c-4be3-ba75-752022e98feb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Faculties has ('9,('Federal University of Technology',),Ondo,2431,12,Engineering)\n"
     ]
    }
   ],
   "source": [
    "fac"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "1a435d1e-71bb-4510-b05e-8096d650ba8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[ Faculties has ('9,('Federal University of Technology',),Ondo,2431,12,Engineering)]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Faculties.all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "dd9da7b2-7659-43e8-b2f3-f88ffa549dbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\" Faculties,9,('Federal University of Technology',),Ondo,2431,12,Engineering)\""
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fac.__repr__()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77eb6699-1a27-4cc6-b261-ffc5530aafe2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
