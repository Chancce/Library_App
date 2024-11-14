// ReturnBookForm.js
import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, Alert } from 'react-bootstrap';

function ReturnBook() {
  const [transactionId, setTransactionId] = useState('');
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/return/', {
        transaction_id: transactionId,
      });
      setMessage({ text: 'Book returned successfully!', variant: 'success' });
    } catch (error) {
      setMessage({ text: error.response?.data?.error || 'Failed to return book', variant: 'danger' });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      {message && <Alert variant={message.variant}>{message.text}</Alert>}
      <Form.Group controlId="transactionId">
        <Form.Label>Transaction ID</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Transaction ID"
          value={transactionId}
          onChange={(e) => setTransactionId(e.target.value)}
          required
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Return Book
      </Button>
    </Form>
  );
}

export default ReturnBook;
