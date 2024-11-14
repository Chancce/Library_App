import React, {useState, useEffect} from 'react'
import { Row, Col } from 'react-bootstrap'
import axios from 'axios'
import Books from '../components/Books'

function Home() {
    const [books,setBooks] = useState([])

    useEffect(() => {
      async function fetchBooks() {
        try {
          const { data } = await axios.get('http://127.0.0.1:8000/api/books/');
          console.log('API Response:', data); // Log the response to see its structure
          setBooks(data.books);
        } catch (error) {
          console.error('Error fetching books:', error);
        }
      }
    
      fetchBooks();
    }, []);

  return (
    <div><h1>Books</h1>
        
    <Row>
      {Array.isArray(books) && books.length > 0 ? (
        books.map(book => (
          <Col key={book.id} sm={12} md={6} lg={4}>
            <Books book={book} />
          </Col>
        ))
      ) : (
        <p>No books available</p> // Display a message if there are no books
      )}
    </Row>
    </div>
  )
}

export default Home