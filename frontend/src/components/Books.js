import React, {useState } from 'react'
import {Card, Button, Modal } from 'react-bootstrap'
import { Link } from 'react-router-dom'

import IssueBook from '../pages/IssueBook'
import ReturnBook from '../pages/ReturnBook'


function Books({ book }) {
    // State to handle modals for issuing and returning books
    const [showIssueModal, setShowIssueModal] = useState(false);
    const [showReturnModal, setShowReturnModal] = useState(false);
  
    const handleIssueModalOpen = () => setShowIssueModal(true);
    const handleIssueModalClose = () => setShowIssueModal(false);
    
    const handleReturnModalOpen = () => setShowReturnModal(true);
    const handleReturnModalClose = () => setShowReturnModal(false);
  
    return (
      <Card className="my-3 p-3 rounded">
        <Link to={`/book/${book.isbn}`} className="text-decoration-none">
          
        </Link>
        
        <Card.Body>
          <Link to={`/book/${book.isbn}`} className="text-decoration-none">
            <Card.Title as="div">
              <strong>{book.title}</strong>
            </Card.Title>
          </Link>
          
          <Card.Text as="div" className="my-3">
            <div className="text-muted">{book.author}</div>
          </Card.Text>
          
          <Card.Text as="div">
            <div
              className={`badge ${book.status === 'available' ? 'bg-success' : book.status === 'checked-out' ? 'bg-warning' : 'bg-danger'}`}
            >
              {book.status}
            </div>
          </Card.Text>
          
          <Card.Text as="div" className="mt-2">
            <small className="text-muted">
              {book.available_count} of {book.stock_count} available
            </small>
          </Card.Text>
  
          <div className="d-flex justify-content-between mt-3">
            <Button variant="secondary" className="w-50" onClick={handleIssueModalOpen}>Issue Book</Button>
            <Button variant="primary" className="w-50" onClick={handleReturnModalOpen}>Return Book</Button>
          </div>
        </Card.Body>
  
        {/* Issue Book Modal */}
        <Modal show={showIssueModal} onHide={handleIssueModalClose}>
          <Modal.Header closeButton>
            <Modal.Title>Issue Book</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <IssueBook bookIsbn={book.isbn} onClose={handleIssueModalClose} />
          </Modal.Body>
        </Modal>
  
        {/* Return Book Modal */}
        <Modal show={showReturnModal} onHide={handleReturnModalClose}>
          <Modal.Header closeButton>
            <Modal.Title>Return Book</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <ReturnBook bookIsbn={book.isbn} onClose={handleReturnModalClose} />
          </Modal.Body>
        </Modal>
      </Card>
    );
  }
  
  export default Books;