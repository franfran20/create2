//SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract FundMeDeployer{

    event FundMeDeployed(address indexed _contract, address indexed _owner);

    function deployFundMe(uint256 _salt, address _owner) public{
        FundMe fundMe = new FundMe{salt: bytes32(_salt)}(_owner);
        emit FundMeDeployed(address(fundMe), _owner);
    }

    function getAddress(uint256 _salt, bytes memory bytecode) public view returns(address){
        bytes32 Hash = keccak256(abi.encodePacked(
            bytes1(0xff), address(this), _salt, keccak256(bytecode)
        ));

        return address(uint160(uint(Hash)));
    }

    function getBytecode(address _owner) public view returns(bytes memory){
        bytes memory bytecode = type(FundMe).creationCode;
        //we add the constructor arguments..
        return abi.encodePacked(bytecode,abi.encode(_owner));
    }
}

contract FundMe{
    address public owner;

    constructor(address _owner){
        owner = owner;
    }

    function fundMe() public payable{
        require(msg.value >= 1e18);
    }

    function withdraw() public {
        require(msg.sender == owner);
        (bool success, bytes memory data) = payable(owner).call{value: address(this).balance}("");
        require(success);
    }
}