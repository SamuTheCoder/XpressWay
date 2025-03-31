import { useState } from 'react'
import './App.css'
import './components/Form/CustomForm.tsx'
import CustomForm from './components/Form/CustomForm.tsx'
import Header from './components/Header/Header.tsx'
import { Button, Alert } from 'react-bootstrap'

function App() {
  const [status, setStatus] = useState("Awaiting Payment");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "danger" | ""; text: string }>({ type: "", text: "" });

  const [creditCard, setCreditCard] = useState('');
  const [expireDate, setExpireDate] = useState('');
  const [cvv, setCvv] = useState('');

  const paymentId = "67e3525bc8bce8b95833cc76"; // Replace with actual ID

  // Function to validate form fields
  const validateForm = () => {
    const cardRegex = /^[0-9]{16}$/;  // Simple 16-digit card number check
    const dateRegex = /^(0[1-9]|1[0-2])\/\d{2}$/;  // MM/YY format
    const cvvRegex = /^[0-9]{3,4}$/;  // CVV: 3 or 4 digits

    if (!cardRegex.test(creditCard)) {
      setMessage({ type: "danger", text: "Invalid credit card number!" });
      return false;
    }
    if (!dateRegex.test(expireDate)) {
      setMessage({ type: "danger", text: "Invalid expiration date (MM/YY)!" });
      return false;
    }
    if (!cvvRegex.test(cvv)) {
      setMessage({ type: "danger", text: "Invalid CVV!" });
      return false;
    }
    
    return true;
  };

  const handlePayment = async () => {
    if (!validateForm()) return; // Stop if validation fails

    setLoading(true);
    setStatus("Processing...");

    setTimeout(async () => {
      try {
        const response = await fetch(`http://localhost:5000/v1/payments/${paymentId}/confirm`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
          throw new Error("Failed to confirm payment");
        }

        setStatus("Payment Successful");
        setMessage({ type: "success", text: status });
      } catch (error) {
        console.error("Error confirming payment:", error);
        setStatus("Payment Failed");
        setMessage({ type: "danger", text: status });
      } finally {
        setLoading(false);
      }
    }, 2000);
  };


  return (
    <>
      <Header/>
      <div className="form-container m-3 p-2">
        <CustomForm onInputChange={(field, value) => {
            if (field === "creditCard") setCreditCard(value);
            if (field === "expireDate") setExpireDate(value);
            if (field === "cvv") setCvv(value);
          }}/>
          <Button variant="success" type="submit" className="w-25 fs-3" onClick={handlePayment} disabled={loading}>
          {loading ? "Processing..." : "Pay"}
          </Button>
      </div>
      <p className="bottom-label">
        {message.text && <Alert variant={message.type} className="mt-3">{message.text}</Alert>}
      </p>
    </>
  )
}

export default App
