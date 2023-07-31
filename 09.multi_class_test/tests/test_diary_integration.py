from lib.diary_entry import DiaryEntry
from lib.diary import Diary 


"""
tests add and all methods returns the full list of instances of Diary Entry
"""

def test_diary_all_method_returns_list_of_diaryentry_instances():
    ellies_diary = Diary()
    entry1 = DiaryEntry("09/09/22", "This is my first diary entry")
    entry2 = DiaryEntry("08/08/23", "This is my second diary entry")
    ellies_diary.add(entry1)
    ellies_diary.add(entry2)
    assert ellies_diary.all() == [entry1, entry2] 


"""
tests count_words method returns correct int of contents of all diary entries 
"""

def test_diary_count_word_method_returns_correct_int():
    ellies_diary = Diary()
    entry1 = DiaryEntry("09/09/22", "This is my first diary entry")
    entry2 = DiaryEntry("08/08/23", "This is my second diary entry")
    ellies_diary.add(entry1)
    ellies_diary.add(entry2)
    assert ellies_diary.count_words() == 12



"""
tests reading time returns expected integer
"""

def test_diary_reading_time_method_returns_expected_int():
    ellies_diary = Diary()
    ellies_diary.add(DiaryEntry("09/09/22", "This is my first diary entry"))
    ellies_diary.add( DiaryEntry("08/08/23", "This is my second diary entry"))
    assert ellies_diary.reading_time(12) == 1
    assert ellies_diary.reading_time(1) == 12
    assert ellies_diary.reading_time(2) == 6


"""
tests find_best_entry_for_reading_time
"""

def test_diary_find_best_entry_method_returns_correct_entry():
    ellies_diary = Diary()
    entry1 = DiaryEntry("09/09/22", "One two three")
    entry2 = DiaryEntry("08/08/23", "One two three four five six seven eight nine ten")
    ellies_diary.add(entry1)
    ellies_diary.add(entry2)
    assert ellies_diary.find_best_entry_for_reading_time(1,10) == entry2
