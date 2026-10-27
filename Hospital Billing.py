# Hospital Billing and Patient Classification System

# Sample hospital charges and payment policy
CONSULTATION_FEE = 500.00
DIAGNOSTIC_FEE = 1000.00
TREATMENT_FEE = 2000.00

SENIOR_CITIZEN_AGE = 60
SENIOR_CITIZEN_DISCOUNT = 10.0
BULK_BILL_THRESHOLD = 5000.00
BULK_BILL_DISCOUNT = 5.0

# Payment classification policy
FULL_PAYMENT_LIMIT = 1000.00
PARTIAL_PAYMENT_LIMIT = 5000.00


def get_valid_integer(prompt, minimum=0):
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Value must be at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_amount(prompt):
    """Read and validate a non-negative monetary amount."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def get_yes_no(prompt):
    """Read a yes/no response."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter yes or no.")


def calculate_bill(age, consultations, diagnostics, treatments):
    """Calculate charges and applicable concessions."""

    consultation_charge = consultations * CONSULTATION_FEE
    diagnostic_charge = diagnostics * DIAGNOSTIC_FEE
    treatment_charge = treatments * TREATMENT_FEE

    subtotal = (
        consultation_charge
        + diagnostic_charge
        + treatment_charge
    )

    # Conditional concessions
    senior_discount = 0.0
    bulk_discount = 0.0

    if age >= SENIOR_CITIZEN_AGE:
        senior_discount = (
            subtotal * SENIOR_CITIZEN_DISCOUNT / 100
        )

    # Apply bulk discount to the amount remaining after
    # the senior citizen concession.
    amount_after_senior = subtotal - senior_discount

    if amount_after_senior >= BULK_BILL_THRESHOLD:
        bulk_discount = (
            amount_after_senior * BULK_BILL_DISCOUNT / 100
        )

    total_discount = senior_discount + bulk_discount
    final_bill = subtotal - total_discount

    return {
        "consultation_charge": consultation_charge,
        "diagnostic_charge": diagnostic_charge,
        "treatment_charge": treatment_charge,
        "subtotal": subtotal,
        "senior_discount": senior_discount,
        "bulk_discount": bulk_discount,
        "total_discount": total_discount,
        "final_bill": final_bill,
    }


def classify_patient(final_bill, amount_paid):
    """Classify payment according to the supplied sample policy."""

    if amount_paid < 0 or amount_paid > final_bill:
        raise ValueError(
            "Payment must be between zero and the final bill."
        )

    balance = round(final_bill - amount_paid, 2)

    if balance == 0:
        classification = "FULLY PAID"
    elif amount_paid == 0:
        classification = "UNPAID"
    elif amount_paid >= FULL_PAYMENT_LIMIT:
        classification = "PARTIALLY PAID - HIGH PAYMENT"
    else:
        classification = "PARTIALLY PAID - LOW PAYMENT"

    return classification, balance


def display_bill(patient, bill, amount_paid, classification, balance):
    """Display the itemized hospital bill."""

    print("\n" + "=" * 60)
    print("              HOSPITAL BILL")
    print("=" * 60)
    print(f"Patient name             : {patient['name']}")
    print(f"Patient age              : {patient['age']}")
    print(f"Patient ID               : {patient['patient_id']}")
    print("-" * 60)

    print("CHARGE DETAILS")
    print(f"Consultation charges     : Rs. {bill['consultation_charge']:.2f}")
    print(f"Diagnostic charges       : Rs. {bill['diagnostic_charge']:.2f}")
    print(f"Treatment charges        : Rs. {bill['treatment_charge']:.2f}")
    print("-" * 60)

    print(f"Subtotal                 : Rs. {bill['subtotal']:.2f}")
    print(
        f"Senior citizen concession: Rs. "
        f"{bill['senior_discount']:.2f}"
    )
    print(f"Bulk bill concession     : Rs. {bill['bulk_discount']:.2f}")
    print(f"Total concessions        : Rs. {bill['total_discount']:.2f}")
    print("-" * 60)

    print(f"FINAL BILL               : Rs. {bill['final_bill']:.2f}")
    print(f"Amount paid              : Rs. {amount_paid:.2f}")
    print(f"Outstanding balance      : Rs. {balance:.2f}")
    print(f"Payment classification   : {classification}")
    print("=" * 60)


def main():
    print("=" * 60)
    print(" HOSPITAL BILLING AND PATIENT CLASSIFICATION SYSTEM")
    print("=" * 60)

    # Patient information
    while True:
        name = input("Enter patient name: ").strip()
        if name:
            break
        print("Patient name cannot be empty.")

    patient_id = input("Enter patient ID: ").strip()
    while not patient_id:
        print("Patient ID cannot be empty.")
        patient_id = input("Enter patient ID: ").strip()

    age = get_valid_integer("Enter patient age: ", minimum=0)

    # Billing quantities
    print("\nEnter service quantities:")
    consultations = get_valid_integer(
        "Number of consultations: "
    )
    diagnostics = get_valid_integer(
        "Number of diagnostic tests: "
    )
    treatments = get_valid_integer(
        "Number of treatments: "
    )

    patient = {
        "name": name,
        "patient_id": patient_id,
        "age": age,
    }

    bill = calculate_bill(
        age, consultations, diagnostics, treatments
    )

    print(f"\nTotal bill after concessions: Rs. {bill['final_bill']:.2f}")

    # Validate payment against the final bill
    while True:
        amount_paid = get_valid_amount(
            "Enter amount paid (Rs.): "
        )

        if amount_paid > bill["final_bill"]:
            print(
                "Error: Payment cannot exceed the final bill. "
                "Please enter the correct amount."
            )
            continue
        break

    classification, balance = classify_patient(
        bill["final_bill"], amount_paid
    )

    display_bill(
        patient,
        bill,
        amount_paid,
        classification,
        balance,
    )

    print("\nBilling process completed successfully.")


if __name__ == "__main__":
    main()
