proc intersect1d(a: [] int, b: [] int, assume_unique: bool) {
  if (!assume_unique) {
	a  = uniqueSort(a, false);
	b = uniqueSort(b, false);
  }
  var aux = radixSortLSD_keys(concatset(a,b));
  const ref head = aux[..aux.domain.high-1];
  const ref tail = aux[aux.domain.low+1..];
  const mask = head == tail;
  return boolIndexer(head, mask);
}