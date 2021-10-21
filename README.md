# Quillpad Transliteration Server

   Quillpad is an indic language input technology that revolutionized the Indian language typing scene. It is one of the most popular Indic input technologies with more than a billion words typed on the website alone.

   > Quillpad pioneered the successful use of machine learning for 
   > building a predictive language input technology. 
   > Quillpad has been rated as the best by many organisations that have embraced Quillpad.

   ### Version
   1.0.1

   ### Preparation
   
   #### Installing Dependencies
   ```
   sudo apt install -y gcc python-dev python-pip python-mysqldb unzip bzip2 mysql-server default-libmysqlclient-dev
   pip install cherrypy Pyrex-real MySQL-python mysql-connector-python cherrypy_cors Nevow tidy
   mkdir logs
   ```
   #### Setting up required files
   There are several archive files in the repository which have to be extracted, these include trained transliteration models and additional text files necessary for the Quillpad Server.  
   Kindly extract all of these archives into the repository folder itself:
   ```
   unzip additional_text_files.zip
   unzip -d unique_word_files unique_word_files.zip
   
   tar -xvf EnglishPronouncingTrees.tar.bz2
   tar -xvf IndianPronouncingTrees.tar.bz2
   tar -xvf bengali.tar.bz2
   tar -xvf gujarati.tar.bz2
   tar -xvf hindi.tar.bz2
   tar -xvf kannada.tar.bz2
   tar -xvf malayalam.tar.bz2
   tar -xvf marathi.tar.bz2
   tar -xvf nepali.tar.bz2
   tar -xvf punjabi.tar.bz2
   tar -xvf tamil.tar.bz2
   tar -xvf telugu.tar.bz2
   ```

   ### Installation

   Quillpad Server requires [Python 2.7](https://www.python.org/downloads/) to run.

   First, we need to compile the Quillpad Model loader that will be used to load the trained transliteration models

   ```sh
   $ cd Python\ Cart/python
   $ python setup.py build_ext --inplace
   $ cp QuillCCart.so ../../
   $ cd ../../
   ```

   Now, the Quillpad Server is ready to run

   ```sh
   $ python startquill_cherry.py
   ```

   ### Additional Information

   * Quillpad runs on port number 8090 (Additional configuration parameters are in *quill_cherry8088.conf*)

   * *processWordJSON* and *processWord* are the API endpoints over which the transliteration server can be accessed.
   > Example:

      * localhost:8090/processWordJSON?inString=hello&lang=hindi
      * localhost:8090/processWordJSON?inString=hello&lang=kannada

   ### Development

   Additional Quillpad Documentation coming soon. Thanks for your patience.

   ### FAQ
   - How to run on port 80?
     - Set port in `quill_cherry8088.conf` and run `sudo -E python startquill_cherry.py`
   - Issue with CherryPy? Use `CherryPy-3.2.2` included within the repo
   - Issue with Pyrex? Download the [source code from here](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/) and use `python setup.py install`
   - Issue with MySQL and MySQL-python?
     - If error during Quillpad server startup, then [check this page](https://stackoverflow.com/questions/43634584/cant-install-mysql-python-with-pip-on-macos-10-12-4/54429707#54429707)
     - If above link also does not work then you may have to download & install via zip files
       - `pip install MySQL-python-1.2.5.zip` --> [Download Link](https://pypi.org/project/MySQL-python/#files)
       - `pip install http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip`
   
   ### References
   An invited talk paper for the Quillpad project:
     https://www.aclweb.org/anthology/W12-4810
   
   Similar Google service integration:
     https://stackoverflow.com/questions/28707899/how-to-use-google-input-tools-in-website
     
   #### More materials
   -  https://www.cse.iitb.ac.in/~anoopk/pages/softwares.html
   -  https://github.com/anoopkunchukuttan/indic_nlp_library
   -  https://github.com/anoopkunchukuttan/transliterator
   -  http://www.cfilt.iitb.ac.in/brahminet/static/publications/brahminet_naacl2015.pdf

   ### To Do
   - Clean the root dir and reorganize data files
   - DB connectivity
   - Python3 support?
