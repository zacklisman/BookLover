import unittest
from booklover import BookLover

class BookloverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        zack_books.add_book("WW2",5)
        self.assertTrue(zack_books.has_read("WW2"))
        
    def test_2_add_book(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        zack_books.add_book("WW2",5)
        zack_books.add_book("WW2",5)
        book_times = 1
        list_book_times = len(zack_books.book_list[zack_books.book_list['book_name'] == 'WW2'])
        self.assertEqual(book_times,list_book_times)
        
    def test_3_has_read(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        zack_books.add_book("WW2",5)
        self.assertTrue(zack_books.has_read("WW2"))
        
    def test_4_has_read(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        self.assertFalse(zack_books.has_read("WW1"))
        
    def test_5_num_books_read(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        test_books = [
            ("Jane Eyre", 4), 
            ("Fight Club", 3),
            ("The Divine Comedy", 5),
            ("The Popol Vuh", 5) 
        ]
        for book in test_books:
            zack_books.add_book(*book)
        self.assertEqual(len(test_books), zack_books.num_books_read())
        
    def test_6_fav_books(self):
        zack_books = BookLover("Zack",'zlisman@yahoo.com','History')
        test_books = [
            ("Jane Eyre", 4), 
            ("Fight Club", 3),
            ("The Divine Comedy", 5),
            ("The Popol Vuh", 5) 
        ]
            
        for book in test_books:
            zack_books.add_book(*book)

        function = len(zack_books.fav_books())
        test = len([x for x, y in test_books if y > 3])
        self.assertEqual(function, test)




if __name__ == '__main__':

    unittest.main(verbosity=3)