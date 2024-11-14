
import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, Alert } from 'react-bootstrap';

function IssueBook() {
  const [memberNumber, setMemberNumber] = useState('');
  const [isbn, setIsbn] = useState('');
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/transactions/issue/', {
        member_number: memberNumber,
        book_isbn: isbn,
      });
      setMessage({ text: 'Book issued successfully!', variant: 'success' });
    } catch (error) {
      setMessage({ text: error.response?.data?.error || 'Failed to issue book', variant: 'danger' });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      {message && <Alert variant={message.variant}>{message.text}</Alert>}
      <Form.Group controlId="memberNumber">
        <Form.Label>Member Number</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Member Number"
          value={memberNumber}
          onChange={(e) => setMemberNumber(e.target.value)}
          required
        />
      </Form.Group>
      <Form.Group controlId="isbn">
        <Form.Label>ISBN</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Book ISBN"
          value={isbn}
          onChange={(e) => setIsbn(e.target.value)}
          required
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Issue Book
      </Button>
    </Form>
  );
}

export default IssueBook;
