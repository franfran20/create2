from brownie import FundMeDeployer, accounts


def deploy():
    SALT = 890
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
    print(f"Address of the deployed fund me: {address_fund_me}")


def main():
    deploy()
