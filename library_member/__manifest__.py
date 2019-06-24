{
 'name': 'library_Member',
 'description': 'Manage people who will be able to borrow books.',
 'author': 'Daniel Reis',
 'depends': ['library_management', 'mail'],
 'application': False,
 'data': [
 'views/book_view1.xml',
'security/library_security.xml',

 'security/ir.model.access.csv',
 'views/book_list.xml',
 'views/library_menu.xml',
 'views/member_view.xml',
 

 ],
}

