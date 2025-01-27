from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

class SolanaUtils:
    def __init__(self, rpc_url: str = "https://api.mainnet-beta.solana.com"):
        """
        Initializes the Solana utility class.
        
        Args:
            rpc_url (str): The RPC URL for the Solana network.
        """
        self.client = Client(rpc_url)

    def get_balance(self, wallet_address: str) -> int:
        """
        Gets the balance of a Solana wallet.
        
        Args:
            wallet_address (str): The wallet address to query.
        
        Returns:
            int: The balance in lamports.
        """
        public_key = PublicKey(wallet_address)
        response = self.client.get_balance(public_key)
        return response["result"]["value"]

    def transfer_sol(self, sender_private_key: str, receiver_address: str, amount: int) -> str:
        """
        Transfers SOL from one wallet to another.
        
        Args:
            sender_private_key (str): The private key of the sender's wallet.
            receiver_address (str): The address of the receiver's wallet.
            amount (int): The amount of SOL to transfer in lamports.
        
        Returns:
            str: The transaction signature.
        """
        sender_public_key = PublicKey(sender_private_key)
        receiver_public_key = PublicKey(receiver_address)
        
        transaction = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_public_key,
                    to_pubkey=receiver_public_key,
                    lamports=amount
                )
            )
        )
        
        response = self.client.send_transaction(transaction, sender_public_key)
        return response["result"]

    def get_transaction_history(self, wallet_address: str, limit: int = 10) -> list:
        """
        Gets the transaction history for a Solana wallet.
        
        Args:
            wallet_address (str): The wallet address to query.
            limit (int): The maximum number of transactions to return.
        
        Returns:
            list: A list of transaction details.
        """
        public_key = PublicKey(wallet_address)
        response = self.client.get_confirmed_signature_for_address2(public_key, limit=limit)
        return response["result"]