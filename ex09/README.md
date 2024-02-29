
- list package
    ```
    pip3 list | grep ft  
    ```
- uninstall package
    ```
    pip3 uninstall
    ```
- ensure package is there
    ```
    pip3 install setuptools wheel
    ```
- create dist
    ```
    python3 setup.py sdist bdist_wheel
    ```
- use dist
    ```
    pip3 install dist/ft_package-0.0.1-py3-none-any.whl
    ```
- show 
    ```
    pip3 show -v ft_package
    ```