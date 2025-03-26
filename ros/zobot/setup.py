from setuptools import find_packages, setup

package_name = "zobot"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/zobot"]),
        ("share/zobot", ["package.xml"]),
        ("share/zobot/launch", ["launch/isaac.launch.py"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="dev",
    maintainer_email="snknitheesh@gmail.com",
    description="Runs isaac-sim natively",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "run_sim = zobot.run_sim:main",
        ],
    },
)
