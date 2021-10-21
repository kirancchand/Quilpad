# -*- coding: utf-8 -*-
# @Date    : Jan 25, 2013
# @Author  : Ram Prakash
# @Version : 1
from os.path import join
xml_folder = "xml"
Xlit_folder = join(xml_folder, "Xlit")
primary_xml_folder = join(xml_folder, "Primary")
key_layouts_folder = join(xml_folder, "Keyboard_Layouts")

langMap = {
    "bengali":   (join(xml_folder, "Bengali_New.xml"),   join("unique_word_files", "unique_bengali_words.txt")),
    "gujarati":  (join(xml_folder, "Gujarati_New.xml"),  join("unique_word_files", "unique_gujarati_words.txt")),
    "hindi":     (join(xml_folder, "Hindi_New.xml"),     join("unique_word_files", "unique_hindi_words.txt")),
    "kannada":   (join(xml_folder, "Kannada_New.xml"),   join("unique_word_files", "unique_kannada_words.txt")),
    "telugu":    (join(xml_folder, "Telugu_New.xml"),    join("unique_word_files", "unique_telugu_words.txt")),
    "tamil":     (join(xml_folder, "Tamil_New.xml"),     join("unique_word_files", "unique_tamil_words.txt")),
    "malayalam": (join(xml_folder, "Malayalam_New.xml"), join("unique_word_files", "unique_malayalam_words.txt")),
    "marathi":   (join(xml_folder, "Marathi_New.xml"),   join("unique_word_files", "unique_marathi_words.txt")),
    "nepali":    (join(xml_folder, "Nepali_New.xml"),    join("unique_word_files", "unique_nepali_words.txt")),
    "punjabi":   (join(xml_folder, "Punjabi_New.xml"),   join("unique_word_files", "unique_punjabi_words.txt"))
}
