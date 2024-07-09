import pytest
import pandas as pd
from update_table import add_item_to_table, remove_item_from_table, increment_item_quantity, decrement_item_quantity


@pytest.fixture
def temp_csv_file(tmp_path):
    """
    Fixture to create a temporary CSV file for testing.
    """
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "temp_table.csv"
    df = pd.DataFrame(columns=["Name", "Price", "Quantity"])

    df.to_csv(p, index=False)
    return str(p)


def test_add_item_to_table(temp_csv_file):
    """
    Test case to verify the functionality of add_item_to_table function.
    """
    add_item_to_table(temp_csv_file, "Apples", 1.99, 10)
    df = pd.read_csv(temp_csv_file)
    assert len(df[df["Name"] == "Apples"]) == 1

def test_increment_item_existing(temp_csv_file):
    """
    Test case to verify the functionality of increment_item_quantity function when incrementing an existing item.
    """
    add_item_to_table(temp_csv_file, "Apples", 1.99, 10)
    df = pd.read_csv(temp_csv_file)
    apples_quantity = df[df["Name"] == "Apples"]["Quantity"].values[0]
    print(f"Number of Apples added to quantity: {apples_quantity}")
    assert apples_quantity == 10

    # now given 10 apples, add 5 more
    increment_item_quantity(temp_csv_file, "Apples", 5)
    df = pd.read_csv(temp_csv_file)
    apples_quantity = df[df["Name"] == "Apples"]["Quantity"].values[0]
    print(f"Number of Apples added to quantity: {apples_quantity}")
    assert apples_quantity == 15


# If you run the test_increment_item_existing test case, you will see that the test fails
def test_increment_item_new(temp_csv_file):
    """
    Test case to verify the functionality of increment_item_quantity function when adding a new item.
    """
    increment_item_quantity(temp_csv_file, "Apples", 5)
    df = pd.read_csv(temp_csv_file)
    apples_quantity = df[df["Name"] == "Apples"]["Quantity"].values[0]
    print(f"Number of Apples added to quantity: {apples_quantity}")
    assert apples_quantity == 5


def test_remove_item_from_table(temp_csv_file):
    """
    Test case to verify the functionality of remove_item_from_table function.
    """
    add_item_to_table(temp_csv_file, "Bananas", 0.99, 5)
    remove_item_from_table(temp_csv_file, "Bananas")
    df = pd.read_csv(temp_csv_file)
    assert len(df[df["Name"] == "Bananas"]) == 0