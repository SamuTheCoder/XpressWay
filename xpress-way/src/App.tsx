import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
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

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const amount = queryParams.get('amount') || "0";
  const currency = queryParams.get('currency') || "USD";
  console.log(amount, currency);
  const [paymentId, setPaymentId] = useState<string | null>(null);
  const productId = queryParams.get('product_id');

  const backendUrl = import.meta.env.VITE_BACKEND_URL; // Get backend URL from .env
  const composerUrl = import.meta.env.VITE_COMPOSER_URL; // Get payments URL from .env

  // Get backend url from .env
  useEffect(() => {
    const initiatePayment = async () => {
      try {
        setLoading(true);
        const response = await fetch(`${backendUrl}v1/payments`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            amount: amount,
            currency: currency,
          }),
        });

        if (!response.ok) {
          throw new Error("Failed to create payment");
        }

        const result = await response.json();
        setPaymentId(result.payment_id);
        console.log("Payment ID:", result.payment_id);
      } catch (error) {
        console.error("Error creating payment:", error);
        
      } finally {
        setLoading(false);
      }
    };

    initiatePayment();
  }, [amount, currency]); 
  // 
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
        const response = await fetch(`${backendUrl}/v1/payments/${paymentId}/confirm`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
          throw new Error("Failed to confirm payment");
        }

        setStatus("Payment Successful");
        setMessage({ type: "success", text: status });
        window.location.href = `${composerUrl}products?paymentId=${paymentId}&productId=${productId}`;
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
        <CustomForm 
          onInputChange={(field, value) => {
            if (field === "creditCard") setCreditCard(value);
            if (field === "expireDate") setExpireDate(value);
            if (field === "cvv") setCvv(value);
          }}
          amount={amount}
          currency={currency}
        />
        <Button variant="success" type="submit" className="w-25 fs-3" onClick={handlePayment} disabled={loading}>
          {loading ? "Processing..." : "Pay"}
        </Button>
      </div>
      <div className="bottom-label">
        {message.text && <Alert variant={message.type} className="mt-3">{message.text}</Alert>}
      </div>
    </>
  )
}

export default App
