{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "829f3a76-4c74-4720-afd3-3aac39fa22a0",
   "metadata": {},
   "source": [
    "# Project : ATM Machine Simulation\n",
    "\n",
    "## Objective\n",
    "To simulate basic ATM operations using Python such as:\n",
    "- Balance check\n",
    "- Cash withdrawal\n",
    "- Cash deposit\n",
    "- PIN validation\n",
    "- Transaction history\n",
    "\n",
    "## Features\n",
    "- Secure PIN authentication\n",
    "- Deposit money\n",
    "- Withdraw money\n",
    "- Check balance\n",
    "- View transaction history\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55dfc2ee-b456-4003-8549-feac7883449b",
   "metadata": {},
   "source": [
    "#  1: Initial Account Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "efd61081-35d0-4e47-a942-8b5c7d7998d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "account = {\n",
    "    \"pin\": \"1234\",\n",
    "    \"balance\": 10000,\n",
    "    \"transactions\": []\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19fa0b54-0a20-48dd-b367-0ef7374a9d39",
   "metadata": {},
   "source": [
    "##  2: PIN Verification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "165dcbff-8960-405f-9048-a5f0cca41873",
   "metadata": {},
   "outputs": [],
   "source": [
    "def verify_pin():\n",
    "    entered_pin = input(\"Enter your ATM PIN: \")\n",
    "    if entered_pin == account[\"pin\"]:\n",
    "        print(\"PIN verified successfully!\")\n",
    "        return True\n",
    "    else:\n",
    "        print(\"Incorrect PIN!\")\n",
    "        return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b23d33b2-ce3b-48c2-8347-bfde8b41d671",
   "metadata": {},
   "source": [
    "##  3: Check Balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4ffa13e2-9d40-43fd-b944-0d79c3d13173",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_balance():\n",
    "    print(f\"Your current balance is: ₹{account['balance']}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba7ddc2a-33e8-47b0-8738-70d94d2ef1cc",
   "metadata": {},
   "source": [
    "##  4: Deposit Money"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3564272f-2736-4696-8d2b-0b8815c94c25",
   "metadata": {},
   "outputs": [],
   "source": [
    "def deposit_money():\n",
    "    amount = float(input(\"Enter amount to deposit: ₹\"))\n",
    "    if amount > 0:\n",
    "        account[\"balance\"] += amount\n",
    "        account[\"transactions\"].append(f\"Deposited ₹{amount}\")\n",
    "        print(f\"₹{amount} deposited successfully!\")\n",
    "    else:\n",
    "        print(\"Invalid deposit amount!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa30df39-5454-48af-ae20-820d2f40eddf",
   "metadata": {},
   "source": [
    "##  5: Withraw Money"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3b7e6098-737e-4faa-87c2-35e4722efd02",
   "metadata": {},
   "outputs": [],
   "source": [
    "def withdraw_money():\n",
    "    amount = float(input(\"Enter amount to withdraw: ₹\"))\n",
    "    if amount <= 0:\n",
    "        print(\"Invalid withdrawal amount!\")\n",
    "    elif amount > account[\"balance\"]:\n",
    "        print(\"Insufficient balance!\")\n",
    "    else:\n",
    "        account[\"balance\"] -= amount\n",
    "        account[\"transactions\"].append(f\"Withdrawn ₹{amount}\")\n",
    "        print(f\"Please collect your cash: ₹{amount}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bc3bb08-8667-4348-bc97-64190489dd27",
   "metadata": {},
   "source": [
    "## 6: Transaction History"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1f6c71ec-9e90-47e3-a31b-516774ca7a1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def transaction_history():\n",
    "    if not account[\"transactions\"]:\n",
    "        print(\"No transactions yet!\")\n",
    "    else:\n",
    "        print(\"Transaction History:\")\n",
    "        for txn in account[\"transactions\"]:\n",
    "            print(\"-\", txn)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a5e1865-9226-4ad4-91cb-db8a1a162737",
   "metadata": {},
   "source": [
    "##  7: ATM Menu\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2a315f74-74a0-4aba-82fd-dfd7f10beebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your ATM PIN:  1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PIN verified successfully!\n",
      "\n",
      "--- ATM MACHINE MENU ---\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Transaction History\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your current balance is: ₹10000\n",
      "\n",
      "--- ATM MACHINE MENU ---\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Transaction History\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter amount to deposit: ₹ 2000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "₹2000.0 deposited successfully!\n",
      "\n",
      "--- ATM MACHINE MENU ---\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Transaction History\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n",
      "Enter amount to withdraw: ₹ 3000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please collect your cash: ₹3000.0\n",
      "\n",
      "--- ATM MACHINE MENU ---\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Transaction History\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transaction History:\n",
      "- Deposited ₹2000.0\n",
      "- Withdrawn ₹3000.0\n",
      "\n",
      "--- ATM MACHINE MENU ---\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Transaction History\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using ATM!\n"
     ]
    }
   ],
   "source": [
    "def atm_menu():\n",
    "    if not verify_pin():\n",
    "        return\n",
    "\n",
    "    while True:\n",
    "        print(\"\\n--- ATM MACHINE MENU ---\")\n",
    "        print(\"1. Check Balance\")\n",
    "        print(\"2. Deposit Money\")\n",
    "        print(\"3. Withdraw Money\")\n",
    "        print(\"4. Transaction History\")\n",
    "        print(\"5. Exit\")\n",
    "\n",
    "        choice = input(\"Enter your choice: \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            check_balance()\n",
    "        elif choice == \"2\":\n",
    "            deposit_money()\n",
    "        elif choice == \"3\":\n",
    "            withdraw_money()\n",
    "        elif choice == \"4\":\n",
    "            transaction_history()\n",
    "        elif choice == \"5\":\n",
    "            print(\"Thank you for using ATM!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice! Try again.\")\n",
    "\n",
    "atm_menu()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
