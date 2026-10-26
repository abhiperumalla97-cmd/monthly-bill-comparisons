
# Progressive Electricity Billing System
# Calculates slab charges, fixed charges, surcharges, rebates,
# monthly bill comparisons, and unusual increases.

from datetime import datetime

# Electricity tariff slabs (units, rate per unit)
SLABS = [
    (100, 1.50),
    (100, 2.50),
    (200, 4.00),
    (float("inf"), 6.00)
]

FIXED_CHARGE = 50.00
SURCHARGE_RATE = 5.0       # Percentage
REBATE_RATE = 5.0           # Percentage
UNUSUAL_INCREASE = 30.0     # Percentage threshold


def calculate_energy_charge(units):
    """Calculate progressive electricity charges."""
    remaining_units = units
    energy_charge = 0.0
    slab_details = []
    previous_limit = 0

    for limit, rate in SLABS:
        slab_units = min(remaining_units, limit)
        if slab_units <= 0:
            break

        charge = slab_units * rate
        energy_charge += charge

        slab_details.append(
            (slab_units, rate, charge)
        )

        remaining_units -= slab_units

        if remaining_units <= 0:
            break

    return energy_charge, slab_details


def calculate_bill(units):
    """Calculate the complete electricity bill."""
    energy_charge, slab_details = calculate_energy_charge(units)

    fixed_charge = FIXED_CHARGE
    subtotal = energy_charge + fixed_charge

    surcharge = subtotal * SURCHARGE_RATE / 100
    rebate = subtotal * REBATE_RATE / 100

    total_bill = subtotal + surcharge - rebate

    return {
        "units": units,
        "energy_charge": energy_charge,
        "slab_details": slab_details,
        "fixed_charge": fixed_charge,
        "surcharge": surcharge,
        "rebate": rebate,
        "total_bill": total_bill
    }


def display_bill(month, bill):
    """Display the bill for a month."""
    print("\n" + "=" * 55)
    print(f"ELECTRICITY BILL - {month}")
    print("=" * 55)
    print(f"Units consumed       : {bill['units']:.2f}")

    print("\nSlab-wise charges:")
    for i, (units, rate, charge) in enumerate(
        bill["slab_details"], start=1
    ):
        print(
            f"Slab {i}: {units:.2f} units x "
            f"Rs.{rate:.2f} = Rs.{charge:.2f}"
        )

    print("-" * 55)
    print(f"Energy charge       : Rs.{bill['energy_charge']:.2f}")
    print(f"Fixed charge        : Rs.{bill['fixed_charge']:.2f}")
    print(f"Surcharge ({SURCHARGE_RATE:.1f}%)     : Rs.{bill['surcharge']:.2f}")
    print(f"Rebate ({REBATE_RATE:.1f}%)         : Rs.{bill['rebate']:.2f}")
    print("-" * 55)
    print(f"TOTAL BILL          : Rs.{bill['total_bill']:.2f}")
    print("=" * 55)


def compare_bills(monthly_bills):
    """Compare monthly bills and identify unusual increases."""
    print("\n\nMONTHLY BILL COMPARISON")
    print("=" * 75)
    print(
        f"{'Month':<18}{'Units':>10}"
        f"{'Bill (Rs.)':>16}{'Change (%)':>16}"
    )
    print("-" * 75)

    previous_bill = None

    for month, bill in monthly_bills:
        if previous_bill is None:
            change_text = "N/A"
        else:
            previous_amount = previous_bill["total_bill"]

            if previous_amount > 0:
                change = (
                    (bill["total_bill"] - previous_amount)
                    / previous_amount
                ) * 100
                change_text = f"{change:+.2f}%"
            else:
                change = 0.0
                change_text = "N/A"

        print(
            f"{month:<18}{bill['units']:>10.2f}"
            f"{bill['total_bill']:>16.2f}"
            f"{change_text:>16}"
        )

        if previous_bill is not None and previous_bill["total_bill"] > 0:
            change = (
                (bill["total_bill"] - previous_bill["total_bill"])
                / previous_bill["total_bill"]
            ) * 100

            if change > UNUSUAL_INCREASE:
                print(
                    f"  WARNING: Unusual bill increase of "
                    f"{change:.2f}% compared with the previous month."
                )

        previous_bill = bill

    print("=" * 75)


def main():
    print("=" * 55)
    print(" PROGRESSIVE ELECTRICITY BILLING SYSTEM")
    print("=" * 55)

    monthly_bills = []

    while True:
        try:
            count = int(input("Enter the number of months to compare: "))
            if count <= 0:
                print("Please enter at least one month.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(count):
        print(f"\nEnter details for month {i + 1}")

        while True:
            month = input(
                "Enter month name (e.g., January 2026): "
            ).strip()
            if month:
                break
            print("Month name cannot be empty.")

        while True:
            try:
                units = float(input("Enter electricity units consumed: "))
                if units < 0:
                    print("Units cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a valid number.")

        bill = calculate_bill(units)
        monthly_bills.append((month, bill))
        display_bill(month, bill)

    compare_bills(monthly_bills)

    print("\nBilling completed successfully.")


if __name__ == "__main__":
    main()
