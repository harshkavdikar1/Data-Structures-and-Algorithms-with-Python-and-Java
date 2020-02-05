package main;

class ListNode<K, V> {
	final int hash;
	final K key;
	V val;
	ListNode<K, V> next;

	ListNode(int h, K k, V v, ListNode<K, V> n) {
		hash = h;
		key = k;
		val = v;
		next = n;
	}
}

public class HashMap<K, V> {
	private int size;
	private ListNode<K, V>[] table;

	public HashMap(int size) {
		table = new ListNode[size];
	}

	public HashMap() {
		this(32);
	}

	public boolean isEmpty() {
		return size == 0 ? true : false;
	}

	public V get(K key) {
		int hash = 0;
		int index = 0;

		if (key != null) {
			hash = key.hashCode();
			index = Math.abs(hash % table.length);
		}

		for (ListNode<K, V> node = table[index]; node != null; node = node.next) {
			if (hash == node.hash && (key == node.key || (key != null && key.equals(node.key)))) {
				return node.val;
			}
		}
		return null;
	}

	public void set(K key, V value) {
		int hash = 0;
		int index = 0;

		if (key != null) {
			hash = key.hashCode();
			index = Math.abs(hash % table.length);
		}

		for (ListNode<K, V> node = table[index]; node != null; node = node.next) {
			if (hash == node.hash && (key == node.key || (key != null && key.equals(node.key)))) {
				node.val = value;
				return;
			}
		}
		ListNode<K, V> node = new ListNode<K, V>(hash, key, value, table[index]);
		table[index] = node;
		size++;
	}

	public boolean remove(K key) {
		int hash = 0;
		int index = 0;

		if (key != null) {
			hash = key.hashCode();
			index = Math.abs(hash % table.length);
		}

		ListNode<K, V> previous = table[index];
		for (ListNode<K, V> node = table[index]; node != null; node = node.next) {
			if (hash == node.hash && (key == node.key || (key != null && key.equals(node.key)))) {
				if (previous == node) {
					table[index] = node.next;
				} else {
					previous.next = node.next;
				}
				previous = node;
				size--;
				return true;
			}
		}
		return false;
	}

	public boolean hasKey(K key) {
		int hash = 0;
		int index = 0;

		if (key != null) {
			hash = key.hashCode();
			index = Math.abs(hash % table.length);
		}

		for (ListNode<K, V> node = table[index]; node != null; node = node.next) {
			if (hash == node.hash && (key == node.key || (key != null && key.equals(node.key)))) {
				return true;
			}
		}
		return false;
	}
}
