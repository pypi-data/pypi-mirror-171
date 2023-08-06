#!/usr/bin/env python
"""
Provides all account functions
"""
import json
import requests
from .urls import ACCOUNT_ADDRESES_URL, ACCOUNT_ASSETS_URL, ACCOUNT_HISTORY_URL, \
    ACCOUNT_INFO_URL, ACCOUNT_LIST_URL, ACCOUNT_REWARDS_URL, ACCOUNT_UPDATES_URL

def get_account_list():
    """
    Get a list of all accounts.

    :return: string list of account (stake address: stake1...  bech32 format) IDs.
    :rtype: list.
    """
    address_list = requests.get(ACCOUNT_LIST_URL, timeout=10)
    address_list = json.loads(address_list.content)
    return address_list


def get_account_info(*args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    get_format = {"_stake_addresses": [args] }
    accounts_info = requests.post(ACCOUNT_INFO_URL, json= get_format , timeout=10)
    accounts_info = json.loads(accounts_info.content)
    return accounts_info

def get_account_rewards(*args):
    """
    Get the full rewards history (including MIR) for given stake addresses (accounts).

    :param str args: Cardano staking address (reward account) in bech32 format (stake1...)
    :param int args: Epoch Number, has to be last parameter (optional).
    return: list with all account rewards.
    :rtype: list.
    """
    epoch = args[len(args)-1]

    if not isinstance(epoch, int):
        get_format = {"_stake_addresses": [args] }
        rewards = requests.post(ACCOUNT_REWARDS_URL, json= get_format , timeout=10)
        rewards = json.loads(rewards.content)
    else:
        get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
        rewards = requests.post(ACCOUNT_REWARDS_URL, json= get_format , timeout=10)
        rewards = json.loads(rewards.content)
    return rewards


def get_account_updates(*args):
    """
    Get the account updates (registration, deregistration, delegation and withdrawals) for given \
    stake addresses (accounts)

    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account updates.
    :rtype: list.
    """
    get_format = {"_stake_addresses": [args]}
    updates = requests.post(ACCOUNT_UPDATES_URL, json= get_format, timeout=10)
    updates = json.loads(updates.content)
    return updates


def get_account_addresses(*args):
    """
    Get all addresses associated with given staking accounts.

    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account addresses.
    :rtype: list.
    """
    get_format = {"_stake_addresses": [args]}
    addresses = requests.post(ACCOUNT_ADDRESES_URL, json= get_format, timeout=10)
    addresses = json.loads(addresses.content)
    return addresses

def get_account_assets(*args):
    """
    Get the native asset balance of given accounts.

    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    get_format = {"_stake_addresses": [args]}
    assets = requests.post(ACCOUNT_ASSETS_URL, json= get_format, timeout=10)
    assets = json.loads(assets.content)
    return assets


def get_account_history(*args):
    """
    Get the staking history of given stake addresses (accounts).

    :param str address: staking address in bech32 format (stake1...)
    return: list with all account history.
    :rtype: list.
    """
    epoch = args[len(args)-1]

    if not isinstance(epoch, int):
        get_format = {"_stake_addresses": [args] }
        history = requests.post(ACCOUNT_HISTORY_URL, json= get_format , timeout=10)
        history = json.loads(history.content)
    else:
        get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
        history = requests.post(ACCOUNT_HISTORY_URL, json= get_format , timeout=10)
        history = json.loads(history.content)
    return history
