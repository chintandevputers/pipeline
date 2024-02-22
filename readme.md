# Setting Up a Virtual Environment

## Prerequisites

- **OS**: Ubuntu 22.04
  - To check your version: `lsb_release -a`
  
- **Python**: Version 3.10.12
  - To verify your version: `python3 -V` or `python3 --version`

- **mage.ai Tool**
  - Mage is an open-source data pipeline tool for transforming and integrating data.


## Setup Instructions

1. Clone this repository and switch to the relevant branch.

2. Create a virtual environment:

    ```bash
    python3 -m venv _travel
    ```

3. Activate the virtual environment:

    ```bash
    source _travel/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements_t.txt
    ```
    OR

    ```bash
    pip install mage-ai
    ```
5. After configuring the necessary configuration files, run:

    ```bash
    mage start travel_info      # travel_info : mage project name
    ```
6. project run on : http://localhost:6789/