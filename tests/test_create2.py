import pytest
from brownie import FundMeDeployer, accounts, network


def test_precomputed_address_is_eqaulto_deployed_address():
    if network.show_active() != "development":
        pytest.skip()
    SALT = 800
    print("Deploying fund me deployer....")
    fundme_deployer = FundMeDeployer.deploy({"from": accounts[0]})
    print("Getting bytecode....")
    bytecode = fundme_deployer.getBytecode(accounts[0].address, {"from": accounts[0]})
    print(f"Bytecode: {bytecode}")
    pre_computed_address = fundme_deployer.getAddress(
        SALT, bytecode, {"from": accounts[0]}
    )
    print(f"Pre-Computed-Address Of Fund Me: {pre_computed_address}")

    tx_deploy_fund_me = fundme_deployer.deployFundMe(
        SALT, accounts[0], {"from": accounts[0]}
    )
    tx_deploy_fund_me.wait(1)

    address_fund_me = tx_deploy_fund_me.events["FundMeDeployed"]["_contract"]

    assert address_fund_me == pre_computed_address


def test_that_if_salt_is_different_addresses_will_be_different():
    if network.show_active() != "development":
        pytest.skip()
    SALT = 800
    SALT2 = 801
    print("Deploying fund me deployer....")
    fundme_deployer = FundMeDeployer.deploy({"from": accounts[0]})
    print("Getting bytecode....")
    bytecode = fundme_deployer.getBytecode(accounts[0].address, {"from": accounts[0]})
    print(f"Bytecode: {bytecode}")
    pre_computed_address = fundme_deployer.getAddress(
        SALT, bytecode, {"from": accounts[0]}
    )
    print(f"Pre-Computed-Address Of Fund Me: {pre_computed_address}")

    tx_deploy_fund_me = fundme_deployer.deployFundMe(
        SALT2, accounts[0], {"from": accounts[0]}
    )
    tx_deploy_fund_me.wait(1)

    address_fund_me = tx_deploy_fund_me.events["FundMeDeployed"]["_contract"]

    assert address_fund_me != pre_computed_address
